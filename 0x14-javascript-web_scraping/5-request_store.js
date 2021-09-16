#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) {
        return console.log(err);
      }
    });
  }
});
