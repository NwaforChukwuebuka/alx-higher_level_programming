#!/usr/bin/node
const { argv } = require('node:process');
const [,, arg1] = argv;
const num = parseInt(arg1);

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
