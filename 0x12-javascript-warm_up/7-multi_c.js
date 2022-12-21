#!/usr/bin/node
/* A Script that prints x times “C is fun”, Where x is the first argument of the script */

const args = process.argv.slice(2);
const num = parseInt(args[0]);
let i = 0;

if (!num) {
  console.log('Missing number of occurrences');
} else {
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}