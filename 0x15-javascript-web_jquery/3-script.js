/*adds the class red to the <header> element when the user clicks on the tag DIV#red_header*/
$(function () {
	$('DIV#red_header').on('click', function () {
		$('header').addClass('red');
	});
});