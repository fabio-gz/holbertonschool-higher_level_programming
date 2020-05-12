#!/usr/bin/node
const request = require('request');

const status = function (response) {
  console.log('code:', response.statusCode);
};

request
  .get(process.argv[2])
  .on('response', status);
