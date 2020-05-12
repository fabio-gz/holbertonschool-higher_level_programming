#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + `${id}`;

const swtitle = function (response, body) {
  console.log(JSON.parse(body).title);
};

request(url, swtitle);
