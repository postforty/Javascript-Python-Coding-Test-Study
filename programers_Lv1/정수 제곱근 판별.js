// https://school.programmers.co.kr/learn/courses/30/lessons/12934?language=javascript
function solution(n) {
  // return Math.sqrt(n) - parseInt(Math.sqrt(n)) > 0
  return Math.sqrt(n) % 1 > 0 ? -1 : Number((Math.sqrt(n) + 1) ** 2);
}

console.log(solution(3));
