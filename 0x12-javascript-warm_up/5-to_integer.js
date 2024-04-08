#!/usr/bin/node
const Number = Math.floor(+process.argv[2]);
console.log(isNaN(Number) ? 'Not a number' : `My number: ${Number}`);
