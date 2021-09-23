#!/usr/bin/node

const myArgs = process.argv.slice(1);
const pathFile = myArgs[1];
const fs = require('fs');
fs.readFile(pathFile, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
