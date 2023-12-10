function solution(number, n, m) {
  // 공배수
  return number % n === 0 && number % m === 0 ? 1 : 0;
}

console.log(solution(60, 2, 3));
