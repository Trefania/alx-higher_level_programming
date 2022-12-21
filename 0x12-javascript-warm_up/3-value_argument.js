#!/usr/bin/node
/* A Script that prints the first argument passed to it */

const args = process.argv.slice(2);

if (!args[0]) {
  console.log('No argument');
} else {
  console.log(args[0]);
}