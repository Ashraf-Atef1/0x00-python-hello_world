$(document).ready(() => $('INPUT#btn_translate').click(() => {
  const langCode = $('INPUT#language_code').val();
  fetch(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`)
    .then(res => res.json()).then(data => $('DIV#hello').text(data.hello));
}));
