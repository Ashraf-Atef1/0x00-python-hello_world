#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const writeData = process.argv[3];

fs.writeFile(filePath, writeData, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
