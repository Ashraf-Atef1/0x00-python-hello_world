#!/usr/bin/node
const request = require('request');
const ID = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${ID}`, (err, res, body) => {
  console.log(JSON.parse(body)["title"]);
  if (err) {
    console.log(err);
  }
});
