#!/usr/bin/node

// Import the process module using the explicit require syntax
const process = require('node:process');

// Extract the arguments excluding the first two elements (path and script name)
const args = process.argv.slice(2);

if (args.length < 2) {
  // If there are less than two arguments, print 0
  console.log(0);
} else {
  // Convert all arguments to integers
  let numbers = args.map(arg => parseInt(arg, 10));

  // Remove duplicates by converting to a Set and back to an array
  let uniqNum = [...new Set(numbers)];

  // Sort the unique numbers in ascending order
  uniqNum.sort((a, b) => a - b);

  // Print the second biggest number
  // Since it's sorted in ascending order, the second biggest is the second last
  console.log(uniqNum[uniqNum.length - 2]);
}
