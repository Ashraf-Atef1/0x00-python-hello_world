fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then(res => res.json()).then(data => $('DIV#character').text(data.name));
