$('#toggle_header').click(function () {
	// checking which class is on and change it to the other one
	if ($('header').hasClass('green')) {
		$('header').removeClass('green').addClass('red');
	} else {
		//we are removing the red class and adding the green one
		$('header').removeClass('red').addClass('green');
	}
});