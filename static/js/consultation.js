// static/js/consultation.js

let localStream = null;
let peerConnection = null;
const configuration = {'iceServers': [{'urls': 'stun:stun.l.google.com:19302'}]};

async function startVideoStream() {
    localStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
    document.getElementById('localVideo').srcObject = localStream;
    initializePeerConnection();
}

function initializePeerConnection() {
    peerConnection = new RTCPeerConnection(configuration);
    localStream.getTracks().forEach(track => {
        peerConnection.addTrack(track, localStream);
    });
    peerConnection.ontrack = handleRemoteStreamAdded;
    peerConnection.onicecandidate = event => {
        if (event.candidate) {
            sendSignal({'ice_candidate': event.candidate});
        }
    };
    createOffer();
}

function handleRemoteStreamAdded(event) {
    const remoteVideo = document.getElementById('remoteVideo');
    remoteVideo.srcObject = event.streams[0];
}

function createOffer() {
    peerConnection.createOffer().then(offer => {
        return peerConnection.setLocalDescription(offer);
    }).then(() => {
        sendSignal({'offer': peerConnection.localDescription});
    });
}

function handleSignal(data) {
    if (data.offer) {
        peerConnection.setRemoteDescription(new RTCSessionDescription(data.offer));
        peerConnection.createAnswer().then(answer => {
            return peerConnection.setLocalDescription(answer);
        }).then(() => {
            sendSignal({'answer': peerConnection.localDescription});
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

document.addEventListener('DOMContentLoaded', startVideoStream);

function sendMessage() {
    const messageInput = document.getElementById('message-input');
    const message = messageInput.value;
    consultationSocket.send(JSON.stringify({ 'message': message }));
    messageInput.value = '';
    appendMessage(message, 'You');
}

function appendMessage(message, sender) {
    const messageList = document.getElementById('message-list');
    const msg = document.createElement('li');
    msg.textContent = `${sender}: ${message}`;
    messageList.appendChild(msg);
}

function sendFile() {
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function() {
            const data = reader.result;
            consultationSocket.send(data);
        };
        reader.readAsArrayBuffer(file);
    }
}

function setupEmojiPicker() {
    const picker = new EmojiPickerElement();
    const input = document.getElementById('message-input');
    picker.addEventListener('emoji-click', event => {
        input.value += event.detail.unicode;
    });
    document.body.appendChild(picker);
}
