#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ntime = 0;

  for (const i of list) {
    if (i === searchElement) {
      ntime += 1;
    }
  }
  return ntime;
};
