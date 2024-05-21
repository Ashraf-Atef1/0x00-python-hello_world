#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let def = {};

request(URL, function (err, res) {
  if (err) {
    console.log(err);
  } else {
    const filmResult = JSON.parse(res.body);
    filmResult.characters.forEach(item => {
      request(item, function (err, res) {
        if (err) {
          console.log(err);
        } else {
          def = JSON.parse(res.body);
          console.log(def.name);
        }
      });
    });
  }
});
