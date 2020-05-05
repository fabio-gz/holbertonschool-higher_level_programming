#!/usr/bin/node
function facto (a) {
  if (a === 1) {
    return a;
  } else {
    return a * facto(a - 1);
  }
}

if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  console.log(facto(process.argv[2]));
}
