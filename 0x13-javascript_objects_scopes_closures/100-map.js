#!/usr/bin/node
const data = require('./100-data').list;
const newData = [];
data.reduce((a, b) => newData.push(a * b), 0);
console.log(newData);
