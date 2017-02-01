function emit(event, message) {
    socket.emit(event, message);
}

function send_message(message) {
    emit('message', message)
    document.getElementById("chat_box").innerHTML += "<div><div class='message client_message'>" + message +"</div></div>";
    // TODO: add this message to
    // TODO: clear message input box
}