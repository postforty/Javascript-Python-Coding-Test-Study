function solution(arr) {
  const start = Math.max(...arr);
  const end = arr.reduce((a, b) => a * b);
  console.log(start);
  console.log(end);

  for (let i = start; i <= end; i++) {
    let result = 0;
    for (let j of arr) {
      if i % j !==
    }
  }

  return;
}

console.log(solution([2, 6, 8, 14])); // 168
// console.log(solution([1, 2, 3])); // 6
// console.log(solution([5, 10, 15, 20, 25])); // 300
// // console.log(solution([1,10,100,1000,5000,3,9999])) // 49995000
// console.log(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])); // 2520
