#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
