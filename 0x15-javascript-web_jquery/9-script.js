$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (char) {
      $('#hello').text(char.hello);
    }
  });
});
