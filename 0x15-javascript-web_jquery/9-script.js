// Fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.
$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
// The translation  must be displayed in the HTML tag DIV#hello.
  $('DIV#hello').text(data.hello);
});
