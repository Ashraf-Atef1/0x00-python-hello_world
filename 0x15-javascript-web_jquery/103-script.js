$(document).ready(() => {
  $('INPUT#btn_translate').click(() => say_hello());
  $(document).on('keypress', function (e) {
    if (e.which == 13) { say_hello(); }
  });
});

function say_hello () {
  const langCode = $('INPUT#language_code').val();
  fetch(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`)
    .then(res => res.json()).then(data => $('DIV#hello').text(data.hello));
}
