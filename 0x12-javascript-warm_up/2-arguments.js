#!/usr/bin/node
let myArgs = process.argv.length

if (myArgs < 3) {
    console.log('No argument');
} else if (myArgs === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
