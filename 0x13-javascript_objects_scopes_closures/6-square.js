#!/usr/bin/node
const lastSquare = require('./5-square.js');

class Square extends lastSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
