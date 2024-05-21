#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let def = {};

request(URL, async function (err, res) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(res.body).characters;
    (function printCharacter (index) {
      request.get(characters[index], function (err, res) {
        if (err) {
          console.log(err);
        } else {
          def = JSON.parse(res.body);
          console.log(def.name);
          if (index < characters.length - 1) {
            printCharacter(++index);
          }
        }
      });
    })(0);
  }
});
