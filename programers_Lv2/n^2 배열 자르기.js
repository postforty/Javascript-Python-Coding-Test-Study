function solution(n, left, right) {
  var answer = [];
  for (let i = left; i <= right; i++) {
    answer.push(Math.max(Math.floor(i / n), i % n) + 1);
  }
  return answer;
}

console.log(solution(3, 2, 5)); // [3,2,2,3]
console.log(solution(4, 7, 14)); // [4,3,3,3,4,4,4,4]
