#!/usr/bin/node
const leng = process.argv.length;

if (leng === 3 || isNaN(process.argv[2])) {
  console.log(0);
} else {
  let bigg;
  let sbigg;
  if (process.argv[2] < process.argv[3]) {
    bigg = process.argv[3];
    sbigg = process.argv[2];
  } else {
    bigg = process.argv[2];
    sbigg = process.argv[3];
  }
  for (let i = 4; i < leng; i++) {
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
