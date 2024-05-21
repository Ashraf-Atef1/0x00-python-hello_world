#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
const ID = 18;

request.get(URL, (err, res, body) => {
  try {
    const results = JSON.parse(body).results
      .filter(film => film.characters.find(e => e.endsWith(`/${ID}/`)));
    console.log(results.length);
  } catch {
    console.log(0);
  }
  if (err) {
    console.log(err);
  }
});
