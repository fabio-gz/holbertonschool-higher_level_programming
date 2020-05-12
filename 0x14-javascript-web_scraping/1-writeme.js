#!/usr/bin/node
const fs = require('fs');

const f1 = process.argv[2];
const error = function (err) {
  if (err) {
    return console.log(err);
  }
};

fs.writeFile(f1, process.argv[3], { encoding: 'utf-8' }, error);
