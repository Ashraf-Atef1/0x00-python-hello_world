#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request.get(URL, (err, res) => {
  console.log(`code: ${res.statusCode}`)
})
