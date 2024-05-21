#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request.get(URL, (err, res) => {
  const results = {};
  JSON.parse(res.body).forEach(task => {
    if (task.completed && results[task.userId] === undefined) {
      results[task.userId] = 1;
    } else if (task.completed) {
      results[task.userId] += 1;
    }
  });
  console.log(results);
  if (err) {
    console.log(err);
  }
});
