#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
const ID = 18;

request.get(URL, (err, res, body) => {
  if (res.statusCode >= 300)
    return console.log(0);
  const results = JSON.parse(body).results
  if (results)
    results.filter(film => film.characters
      .includes(`https://swapi-api.alx-tools.com/api/people/${ID}/`)).length;
  console.log(results);
  if (err) {
    console.log(err);
  }
});
