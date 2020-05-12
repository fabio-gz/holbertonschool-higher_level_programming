#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const wr = function (err, response, body) {
  if (err) {
    return console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, { encoding: 'utf-8' }, function (err) {
      if (err) {
        return console.log(err);
      }
    });
  }
};

request(url, wr);
