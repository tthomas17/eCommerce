function showFlashMessage(message){
		var template = "<div class='container flash-alert-box'>" +
		"<div class='col-sm-3 col-sm-offset-8'>" +
		"<div class='alert alert-success alert-dismissible' role='alert'>" +
		"<button type='button' class='close' data-dismiss='alert' aria-label='Close'>"+
		"<span aria-hidden='true'>&times;</span></button>" + message + "</div></div></div>"
		$("body").append(template);
		$(".flash-alert-box").fadeIn();
		setTimeout(function(){
			$(".flash-alert-box").fadeOut();
		}, 1800);
	}


