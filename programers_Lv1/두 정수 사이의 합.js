// https://school.programmers.co.kr/learn/courses/30/lessons/12912?language=javascript
function solution(a, b) {
  const arr = Array.from(
    { length: Math.abs(a - b) + 1 },
    (_, i) => i + (a > b ? b : a)
  );
  return arr.reduce((acc, curr) => (acc += curr));
}

console.log(solution(3, 5));
