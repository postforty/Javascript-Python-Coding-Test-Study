// https://school.programmers.co.kr/learn/courses/30/lessons/12931?language=javascript
function solution(n) {
  return [...String(n)].reduce((acc, curr) => {
    acc += curr * 1;
    return acc;
  }, 0);
}

console.log(solution(123));
