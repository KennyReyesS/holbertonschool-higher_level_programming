#!/usr/bin/node

const myArgs = process.argv.slice(1);
const pathFile = myArgs[1];
const stringWrite = myArgs[2];
const fs = require('fs');
fs.writeFile(pathFile, stringWrite, function (err) {
  if (err) {
    return console.log(err);
  }
});
