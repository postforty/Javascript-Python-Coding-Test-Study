// https://school.programmers.co.kr/learn/courses/30/lessons/12933?language=javascript
function solution(n) {
  return [...String(n)].sort((a, b) => b - a).join("") * 1;
}

console.log(solution(118372));
