// adds a <li> element to a list when the user clicks on the tag DIV#add_item
$('DIV#add_item').click(function () {
	$('<li>Item</li>').appendTo('.my_list');
	//adding an element to the my_list
});