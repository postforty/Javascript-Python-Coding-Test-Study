// https://school.programmers.co.kr/learn/courses/30/lessons/12932
function solution(n) {
  return [...String(n)].reverse().map((el) => Number(el));
}

console.log(solution(123456789));
