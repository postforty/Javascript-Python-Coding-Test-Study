// https://school.programmers.co.kr/learn/courses/30/lessons/70128?language=javascript
function solution(a, b) {
  const answer = a.reduce((acc, curr, idx) => {
    acc += curr * b[idx];
    return acc;
  }, 0);
  return answer;
}

console.log(solution([1, 2, 3, 4], [-3, -1, 0, 2]));
