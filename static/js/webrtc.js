// static/js/webrtc.js

document.addEventListener('DOMContentLoaded', async function() {
    // Запускаем видео потоки как только DOM загружен
    await startVideoCall();
});

async function startVideoCall() {
    const localVideo = document.getElementById('localVideo');
    const remoteVideo = document.getElementById('remoteVideo');
    let localStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
    localVideo.srcObject = localStream;

    const configuration = {'iceServers': [{'urls': 'stun:stun.l.google.com:19302'}]};
    const peerConnection = new RTCPeerConnection(configuration);

    localStream.getTracks().forEach(track => {
        peerConnection.addTrack(track, localStream);
    });

    peerConnection.ontrack = function({ streams }) {
        remoteVideo.srcObject = streams[0];
    };

    peerConnection.onicecandidate = function(event) {
        if (event.candidate) {
            sendSignal({ 'ice_candidate': event.candidate });
        }
    };

    // Создаем оффер и устанавливаем его как локальное описание
    const offer = await peerConnection.createOffer();
    await peerConnection.setLocalDescription(offer);
    sendSignal({ 'offer': offer });

    // Обработчики сообщений для сигнализации
    consultationSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        handleSignal(data, peerConnection);
    };
}

function sendSignal(message) {
    consultationSocket.send(JSON.stringify(message));
}

async function handleSignal(data, peerConnection) {
    if (data.offer) {
        await peerConnection.setRemoteDescription(new RTCSessionDescription(data.offer));
        const answer = await peerConnection.createAnswer();
        await peerConnection.setLocalDescription(answer);
        sendSignal({ 'answer': answer });
    } else if (data.answer) {
        await peerConnection.setRemoteDescription(new RTCSessionDescription(data.answer));
    } else if (data.ice_candidate) {
        await peerConnection.addIceCandidate(new RTCIceCandidate(data.ice_candidate));
    }
}
