#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(1);
const url = myArgs[1];

request(url, function (error, response, body) {
  const respJson = JSON.parse(body);
  if (error) {
    console.log(error);
  } else {
    let n = 0;
    for (const i in respJson.results) {
      const characters = respJson.results[i].characters;
      for (const urlid in characters) {
        if (characters[urlid] === 'https://swapi-api.hbtn.io/api/people/18/') {
          n++;
        }
      }
    }
    console.log(n);
  }
});
