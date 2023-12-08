// https://school.programmers.co.kr/learn/courses/30/lessons/12922?language=javascript
function solution(n) {
  const sArr = ["수", "박"];
  let answer = "";
  Array.from({ length: n }, (_, i) => i).forEach((_, i) => {
    answer += i % 2 === 0 ? sArr[0] : sArr[1];
  });
  return answer;
}

console.log(solution(3));
