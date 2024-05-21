#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
const ID = 18;

request.get(URL, (err, res, body) => {
  try {
    const results = JSON.parse(body).results
      .filter(film => film.characters
        .includes(`https://swapi-api.alx-tools.com/api/people/${ID}/`)).length;
    console.log(results);
  } catch {
    console.log(0);
  }
  if (err) {
    console.log(err);
  }
});
