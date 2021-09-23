#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(1);
const url = myArgs[1];

request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
