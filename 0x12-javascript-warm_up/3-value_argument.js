#!/usr/bin/node
const myArgs = process.argv.slice(2);

if (myArgs[0] === undefined) {
  console.log('No argument');
} else {
  console.log(myArgs[0])
}
