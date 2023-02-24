/* fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
ANOTHER WAY
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').html(data.name);
});*/

$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json",
	function (data) {
		$("DIV#character").text(data.name);
	});