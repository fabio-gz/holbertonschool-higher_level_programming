#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const ocurr = parseInt(process.argv[2]);
  for (let i = 0; i < ocurr; i++) {
    console.log('C is fun');
  }
}
