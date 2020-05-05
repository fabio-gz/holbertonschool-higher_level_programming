#!/usr/bin/node
const leng = process.argv.length;

if (leng === 3 || isNaN(process.argv[2])) {
  console.log(0);
} else {
  let bigg = process.argv[1];
  let sbigg = process.argv[0];
  for (let i = 2; i < leng; i++) {
    if (process.argv[i] > bigg) {
      sbigg = bigg;
      bigg = process.argv[i];
      continue;
    }
    if (process.argv[i] > sbigg) {
      sbigg = process.argv[i];
    }
  }
  console.log(sbigg);
}
