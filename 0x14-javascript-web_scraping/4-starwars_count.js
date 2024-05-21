#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request.get(URL, (err, res, body) => {
  const results = JSON.parse(body).results
    .filter(film => film.characters
      .includes('https://swapi-api.alx-tools.com/api/people/18/')).length;
  console.log(results);
  if (err) {
    console.log(err);
  }
});
