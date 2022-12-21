#!/usr/bin/node
/* A Script that computes and prints a factorial */

const args = process.argv.slice(2);
const num = parseInt(args[0]);
const res = factorial(num);
console.log(res);

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}