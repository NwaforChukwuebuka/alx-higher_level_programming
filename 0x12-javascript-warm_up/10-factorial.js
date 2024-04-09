#!/usr/bin/node

// Import the process module using the explicit require syntax
const process = require('node:process');

// Recursive function to compute factorial
function factorial (n) {
  if (isNaN(n) || n <= 1) { // Base case: if n is not a number or n <= 1
    return 1;
  }
  return n * factorial(n - 1); // Recursive call
}

// Extract the first argument from command line
const [, , arg] = process.argv;

// Parse the argument as an integer
const num = parseInt(arg, 10);

// Compute and print the factorial of the number
console.log(factorial(num));
