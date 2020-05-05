#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const ocurr = parseInt(process.argv[2]);
  for (let i = 0; i < ocurr; i++) {
    console.log('X'.repeat(ocurr));
  }
}
