#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');

request.get(URL, (err, res, body) => {
  fs.writeFile(filePath, res.body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
  if (err) {
    console.log(err);
  }
});
