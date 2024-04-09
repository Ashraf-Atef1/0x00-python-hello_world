#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.map((e) => e === searchElement && count++);
  return (count);
};
