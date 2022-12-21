#!/usr/bin/node

const args = process.argv.slice(2);
const len = args.length;

if (len < 1) {
  console.log('No argument');
} else if (len === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
