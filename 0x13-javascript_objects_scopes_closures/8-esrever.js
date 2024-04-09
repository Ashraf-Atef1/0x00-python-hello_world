#!/usr/bin/node
exports.esrever = function (list) {
  const newArray = [];
  list.map(e => newArray.unshift(e));
  return newArray;
};
