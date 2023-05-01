let n = 2;
let arr = ["hello", "one", "even", "never", "now", "world", "draw"];

// forEach를 이용
// const newArr = new Array(arr.length);
// const result = [];
// newArr.fill(1);
// newArr.forEach((_, idx) => {
//   if ((idx + 1) % n === 0) {
//     result.push(n);
//   } else {
//     result.push((idx + 1) % n);
//   }
// });

// const newArr = new Array(arr.length);
// const result = [];
// newArr.fill(1);
// let num = 1;
// newArr.forEach((_, idx) => {
//   if ((idx + 1) % n === 0) {
//     result.push(num);
//     num++;
//   } else {
//     result.push(num);
//   }
// });

// let num = 1;
// const result = arr.map((el, idx) => {
//   if ((idx + 1) % n === 0) {
//     return n;
//   } else {
//     return (idx + 1) % n;
//   }
// });
// [ 1, 2, 1, 2, 1, 2, 1]

let num = 1;
const result = arr.map((el, idx) => {
  if ((idx + 1) % n === 0) {
    let temp = num;
    num++;
    return temp;
  } else {
    return num;
  }
});

console.log(result);
