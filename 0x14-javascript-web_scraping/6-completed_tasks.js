#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(1);
const url = myArgs[1];

request(url, function (error, response, body) {
  const respJson = JSON.parse(body);
  if (error) {
    console.log(error);
  } else {
    const total = {};
    for (const i in respJson) {
      if (respJson[i].completed) {
        if (!(respJson[i].userId in total)) {
          total[respJson[i].userId] = 1;
        } else {
          total[respJson[i].userId] += 1;
        }
      }
    }
    console.log(total);
  }
});
