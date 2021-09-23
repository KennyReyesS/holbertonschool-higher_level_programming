// Adds a <li> element to a list when the user clicks on the tag DIV#add_item:
$('#add_item').click(function (event) {
  const item = '<li>Item</li>';
  $('UL.my_list').append(item);
});
