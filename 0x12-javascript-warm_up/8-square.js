#!/usr/bin/node
/* A Script that prints a square, Where the first argument is the size of square. */

const args = process.argv.slice(2);
const num = parseInt(args[0]);
let i = 0;
const word = 'X';

if (!num) {
  console.log('Missing size');
} else {
  while (i < num) {
    console.log(word.repeat(num));
    i++;
  }
}