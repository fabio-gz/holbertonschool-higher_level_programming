$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (char) {
      for (const i in char.results) {
        $('#list_movies').append('<li>' + char.results[i].title + '</li>');
      }
    }
  });
});
