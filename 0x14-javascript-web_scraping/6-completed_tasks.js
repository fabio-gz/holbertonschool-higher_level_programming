#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const list1 = [];
const dic1 = {};
const compl = function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const dat = JSON.parse(body);
    for (const i in dat) {
      if (dat[i].completed === true) {
        list1.push(dat[i].userId);
      }
    }
    list1.forEach(function (j) { dic1[j] = (dic1[j] || 0) + 1; });
    console.log(dic1);
  }
};

request(url, compl);
