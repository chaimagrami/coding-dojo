/* 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)
  hasOwnProperty()
*/
var user = {username:"John", age:35}

// console.log(user.hasOwnProperty('age'));
// console.log(user.hasOwnProperty('email'));

const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};
// {} do you have "a" as key -- > false - > {a:1}
// {}
const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

function makeFrequencyTable(arr) {
    var expected = {}
    for(var i=0; i<arr.lenght; i++){
        if(expected.hasOwnProperty
    }
}