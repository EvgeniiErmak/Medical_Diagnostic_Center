let localStream = null;
let peerConnection = null;
const configuration = {'iceServers': [{'urls': 'stun:stun.l.google.com:19302'}]};  // Это STUN сервер Google, для локальной разработки это нормально.

async function startVideoStream() {
    localStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
    document.getElementById('localVideo').srcObject = localStream;
}

function handleRemoteStreamAdded(event) {
    const remoteVideo = document.getElementById('remoteVideo');
    remoteVideo.srcObject = event.streams[0];
}

function createOffer() {
    peerConnection = new RTCPeerConnection(configuration);
    localStream.getTracks().forEach(track => {
        peerConnection.addTrack(track, localStream);
    });
    peerConnection.ontrack = handleRemoteStreamAdded;
    peerConnection.createOffer().then(offer => {
        peerConnection.setLocalDescription(offer);
        sendSignal({'offer': offer});
    });
}

function handleSignal(data) {
    if (data.offer) {
        peerConnection.setRemoteDescription(new RTCSessionDescription(data.offer));
        peerConnection.createAnswer().then(answer => {
            peerConnection.setLocalDescription(answer);
            sendSignal({'answer': answer});
        });
    } else if (data.answer) {
        peerConnection.setRemoteDescription(new RTCSessionDescription(data.answer));
    } else if (data.ice_candidate) {
        peerConnection.addIceCandidate(new RTCIceCandidate(data.ice_candidate));
    }
}

function sendSignal(message) {
    consultationSocket.send(JSON.stringify(message));
}

consultationSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    handleSignal(data);
};

document.addEventListener('DOMContentLoaded', startVideoStream);
