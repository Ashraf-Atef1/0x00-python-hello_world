#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let def = {};

request(URL, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const filmResult = JSON.parse(body);
    filmResult.characters.forEach(function (item, index, array) {
      request(item, function (err, res, content) {
        if (err) {
          console.log(err);
        } else {
          def = JSON.parse(content);
          console.log(def.name);
        }
      });
    });
  }
});
