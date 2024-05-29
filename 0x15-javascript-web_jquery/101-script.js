$(document).ready(() => {
  $('DIV#add_item').click(() =>
    console.log($('UL.my_list').append('<li>Item</li>')));
  $('DIV#remove_item').click(() =>
    $('UL.my_list li').first().remove());
  $('DIV#clear_list').click(() =>
    $('UL.my_list li').remove());
});
