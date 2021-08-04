#!/usr/bin/node
const myList = require('./100-data.js');

const newList = myList.list.map((x, index) => x * index);
console.log(myList.list);
console.log(newList);
