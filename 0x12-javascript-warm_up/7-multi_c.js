#!/usr/bin/node
let Number = Math.floor(+process.argv[2]);
const Text = 'C is fun';

while (Number > 0) {
  console.log(Text);
  Number--;
}
isNaN(Number) && console.log('Missing number of occurrences');
