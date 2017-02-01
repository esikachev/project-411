var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function () {
    emit('message', 'I\'m connected!');
});
socket.on('message', function(data){
    print_message('bot_message', data);
});

function emit(event, message) {
    socket.emit(event, message);
}

function send_message(message) {
    emit('message', message)
    print_message('client_message', message)
    // TODO: clear message input box
}

function print_message(owner, message) {
    document.getElementById("chat_box").innerHTML +=
        "<div><div class='message " + owner + "'>" + message + "</div></div>";
}