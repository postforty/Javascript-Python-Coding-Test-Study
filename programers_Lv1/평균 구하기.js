// https://school.programmers.co.kr/learn/courses/30/lessons/12944?language=javascript
function solution(arr) {
  return arr.reduce((acc, curr) => (acc += curr)) / arr.length;
}

console.log(solution([1, 2, 3, 4]));
