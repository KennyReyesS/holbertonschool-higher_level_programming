#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(1);
const urlId = myArgs[1];
const url = 'https://swapi-api.hbtn.io/api/films/';
const urlComplete = url + urlId;

request(urlComplete, function (error, response, body) {
  const respJson = JSON.parse(body);
  if (error) {
    console.log(error);
  } else {
    console.log(respJson.title);
  }
});
