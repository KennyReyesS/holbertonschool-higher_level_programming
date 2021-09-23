// Fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json.
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
// All movie titles must be list in the HTML tag UL#list_movies.
  $.each(data.results, function (i, results) {
    $('UL#list_movies').append('<li>' + results.title + '</li>');
  });
});
