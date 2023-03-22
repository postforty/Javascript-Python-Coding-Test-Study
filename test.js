const arr = [
  [128.63362792028676, 35.2215073061068],
  [128.63362792028676, 35.2215073061068],
];

const newArr = [];
const obj = {};

for (const el of arr) {
  obj["lat"] = el[1];
  obj["lng"] = el[0];
  newArr.push(obj);
}

console.log(newArr);

// console.log(arr.map((el) => JSON.parse(`{"lat": ${el[1]}, "lng": ${el[0]}}`)));
// console.log(
//   tempArr[0].map(el => JSON.parse(`{"lat": ${el[1]}, "lng": ${el[0]}}`)),
//   // tempArr[0].map(el => `{"lat": ${el[1]}, "lng": ${el[0]}}`),
// );
