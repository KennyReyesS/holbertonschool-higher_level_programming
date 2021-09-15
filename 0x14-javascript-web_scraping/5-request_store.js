#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const url = myArgs[2];
const pathFile = myArgs[3];
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(pathFile, body, function (err) {
      if (err) {
        return console.log(err);
      }
    });
  }
});
