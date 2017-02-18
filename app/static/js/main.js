$('.chat[data-chat=person]').addClass('active-chat');
$('.person[data-chat=person]').addClass('active');

$('.left .person').mousedown(function(){
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
        $('.chat[data-chat = '+findChat+']').addClass('active-chat');
    }
});

function sendMessage(){
	var rand = Math.random() * 10;
	var newDiv = document.createElement("div");
	var objDiv = document.getElementById("chat");
	var inputValue = document.getElementById('message_box').value;
	
	newDiv.innerHTML = inputValue;
	
	document.getElementById('message_box').value = '';
	
	if(rand < 5){
		newDiv.className += " bubble you";
	}
	else{
		newDiv.className += " bubble me";
	}
	
	objDiv.appendChild(newDiv);
	objDiv.scrollTop = objDiv.scrollHeight;
	
	emit('message', inputValue);
}


var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
socket.on('connect', function () {
    emit('status', 'I\'m connected!');
});

socket.on('message', function(data){
    print_message('bot_message', data);
});

function emit(event, message) {
    socket.emit(event, message);
}

document.addEventListener("keydown", function (e) {
    if (e.keyCode === 13) {
        sendMessage();
    }
});