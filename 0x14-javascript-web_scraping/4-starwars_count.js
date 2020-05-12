#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const wedge = "https://swapi-api.hbtn.io/api/people/18/";

const numfilms = function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const dat = JSON.parse(body).results;
    let num = 0;
    for (const i of dat) {
      for (const j of i.characters) {
        if (j === wedge) {
          num++;
        }
      }
    }
    console.log(num);
  }
};

request(url, numfilms);
