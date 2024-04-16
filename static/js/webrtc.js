async function startVideoCall() {
    const localVideo = document.getElementById('localVideo');
    const remoteVideo = document.getElementById('remoteVideo');

    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
    localVideo.srcObject = stream;

    const peerConnection = new RTCPeerConnection();

    stream.getTracks().forEach(track => {
        peerConnection.addTrack(track, stream);
    });

    peerConnection.ontrack = function({ streams }) {
        remoteVideo.srcObject = streams[0];
    };

    // Также вам нужно реализовать сигнализацию для обмена предложениями и ответами
    // Это можно сделать через WebSocket, который вы уже начали использовать
}

document.addEventListener('DOMContentLoaded', startVideoCall);
