$('.chat[data-chat=person]').addClass('active-chat');
$('.person[data-chat=person]').addClass('active');

$('.left .person').mousedown(function () {
    if ($(this).hasClass('.active')) {
        return false;
    }
    else {
        var findChat = $(this).attr('data-chat');
        var personName = $(this).find('.name').text();

        $('.right .top .name').html(personName);
        $('.chat').removeClass('active-chat');
        $('.left .person').removeClass('active');
        $(this).addClass('active');
        $('.chat[data-chat = ' + findChat + ']').addClass('active-chat');
    }
});

function sendMessage() {
    var inputValue = document.getElementById('message_box').value;

    document.getElementById('message_box').value = '';

    emit('message', inputValue);

    printMessage("me", inputValue)
}

function printMessage(sender, message) {
    var newDiv = document.createElement("div");
    var objDiv = document.getElementById("chat");

    newDiv.innerHTML = message;
    newDiv.className += " bubble" + " " + sender;

    objDiv.appendChild(newDiv);
    objDiv.scrollTop = objDiv.scrollHeight;
}


var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
socket.on('connect', function () {
    emit('status', 'I\'m connected!');
});

socket.on('message', function (data) {
    printMessage('you', data);
});

function emit(event, message) {
    socket.emit(event, message);
}

document.addEventListener("keydown", function (e) {
    if (e.keyCode === 13) {
        sendMessage();
    }
});