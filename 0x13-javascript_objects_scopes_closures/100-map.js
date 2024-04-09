#!/usr/bin/node
const data = require('./100-data').list;
let oldNum = 0;
const newData = data.map((e) => {
  const tmp = oldNum;
  oldNum = e;
  return e * tmp;
});
console.log(data);
console.log(newData);
