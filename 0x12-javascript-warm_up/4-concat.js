#!/usr/bin/node
const { argv } = require('node:process');
const [,, arg1, arg2] = argv;
console.log(arg1 + ' is ' + arg2);
