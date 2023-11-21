// https://school.programmers.co.kr/learn/courses/30/lessons/12954?language=javascript
function solution(x, n) {
  let addX = 0;
  const answer = Array.from({ length: n }, (_, i) => {
    addX += x;
    return addX;
  });
  return answer;
}

console.log(solution(2, 5));
