#!/usr/bin/node
const list1 = require('./100-data').list;
console.log(list1);

const map1 = list1.map((x, i) => x * i);
console.log(map1);
