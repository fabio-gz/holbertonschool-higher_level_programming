#!/usr/bin/node
const fs = require('fs');
const f1 = './' + process.argv[2];
const f2 = './' + process.argv[3];

const data1 = fs.readFileSync(f1);
const data2 = fs.readFileSync(f2);

fs.writeFileSync(process.argv[4], data1 + data2);
