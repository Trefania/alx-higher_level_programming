#!/usr/bin/node
/* A Script that prints the addition of 2 integers */

const args = process.argv.slice(2);
const num = parseInt(args[0]);
const num2 = parseInt(args[1]);
const res = add(num, num2);
console.log(res);

function add (a, b) {
  return a + b;
}