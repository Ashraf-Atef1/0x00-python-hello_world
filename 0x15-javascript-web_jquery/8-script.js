fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then(res => res.json()).then(data => data.results).then(results => {
    const listElement = $('UL#list_movies');
    for (let i = 0; i < results.length; i++) { listElement.append(`<li>${results[i].title}</li>`); }
  });
