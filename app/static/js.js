var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
    emit('message', 'I\'m connected!');
});

function emit(event, message) {
    socket.emit(event, message);
}

function send_message(message) {
    emit('message', message)
    document.getElementById("chat_box").innerHTML += "<div><div class='message client_message'>" + message +"</div></div>";
    // TODO: clear message input box
}