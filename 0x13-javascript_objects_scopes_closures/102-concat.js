#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, firstFileData) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.readFile(process.argv[3], 'utf-8', (err, secondFileData) => {
    if (err) {
      console.error(err);
      return;
    }
    fs.writeFile(process.argv[4], firstFileData + secondFileData, err => {
      if (err) {
        console.error(err);
      }
    });
  });
});
