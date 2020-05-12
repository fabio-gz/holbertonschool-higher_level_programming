#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + `${id}`;

const char = function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const url2 = JSON.parse(body).characters;
    for (const i in url2) {
      request(url2[i], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
};

request(url, char);
