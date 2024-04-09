#!/usr/bin/node

const { argv } = require('node:process');

const [,, x] = argv;

const num = parseInt(x);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
