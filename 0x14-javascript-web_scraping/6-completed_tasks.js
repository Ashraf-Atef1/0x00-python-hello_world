#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request.get(URL, (err, res) => {
  const results = {};
  JSON.parse(res.body).map(task => {
    if (results[task.userId] === undefined) {
      results[task.userId] = 0;
    }
    results[task.userId] += task.completed;
    return task;
  });
  console.log(results);
  if (err) {
    console.log(err);
  }
});
