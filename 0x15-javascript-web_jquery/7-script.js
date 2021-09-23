// Fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json.
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (char) {
// The name must be displayed in the HTML tag DIV#character.
  $('DIV#character').text(char.name);
});
