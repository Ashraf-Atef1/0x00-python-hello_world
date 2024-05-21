#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
const ID = 18;

request.get(URL, (err, res, body) => {
  if (!err && res.statusCode < 300) {
    const results = JSON.parse(body).results
      .filter(film => film.characters
        .includes(`https://swapi-api.alx-tools.com/api/people/${ID}/`)).length;
    console.log(results);
  } else {
    console.log(0);
  }
});
