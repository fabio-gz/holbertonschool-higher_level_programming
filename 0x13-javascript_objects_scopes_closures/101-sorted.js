#!/usr/bin/node
const dict1 = require('./101-data').dict;

const dict2 = Object.keys(dict1).reduce((v, k) => {
  const val = dict1[k];
  v[val] = v[val] || [];
  v[val].push(k);
  return v;
}, {});
console.log(dict2);
