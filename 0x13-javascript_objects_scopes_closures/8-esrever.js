#!/usr/bin/node
exports.esrever = function (list) {
  const revl = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revl.push(list[i]);
  }
  return revl;
};
