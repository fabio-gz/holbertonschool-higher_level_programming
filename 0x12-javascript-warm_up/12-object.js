#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

function upd (persona) {
  persona.value = 89;
  return persona.value;
}
upd(myObject);
console.log(myObject);
