var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function () {
    emit('status', 'I\'m connected!');
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
    document.getElementById('message_box').value = "";
}

function print_message(owner, message) {
    document.getElementById("chat_box").innerHTML +=
        "<div><div class='message " + owner + "'>" + message + "</div></div>";
}

document.addEventListener("keydown", function (e) {
    if (e.keyCode === 13) {
        send_message(document.getElementById('message_box').value);
    }
});