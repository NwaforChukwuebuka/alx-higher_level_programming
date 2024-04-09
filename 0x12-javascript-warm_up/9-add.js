#!/usr/bin/node

// Import the process module using the explicit require syntax
const process = require('node:process');

// Function to add two integers
function add (a, b) {
  console.log(a + b);
}

// Extract command line arguments with descriptive names using destructuring
const [, , arg1, arg2] = process.argv;

// Convert arguments to integers
const num1 = parseInt(arg1, 10);
const num2 = parseInt(arg2, 10);

// Call the function with the parsed integers
add(num1, num2);
