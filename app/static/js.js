function emit(event, message) {
    socket.emit(event, message);
}

function send_message(object) {
    emit('message', object.textContent)
    // TODO: clear message input box
}