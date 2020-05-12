#!/usr/bin/node
const fs = require('fs');
const f1 = process.argv[2];

const error = function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
};

fs.readFile(f1, { encoding: 'utf-8' }, error);
