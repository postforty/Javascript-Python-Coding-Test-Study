function solution(n, a, b) {
  var answer = 0;

  const arr = new Array(n);
  arr.fill(0);
  arr[a - 1] = 1;
  arr[b - 1] = 2;

  return arr;
}

console.log(solution(8, 4, 7)); // 3
// console.log(solution(8, 3, 7)); // 3
// console.log(solution(8, 2, 7)); // 3
