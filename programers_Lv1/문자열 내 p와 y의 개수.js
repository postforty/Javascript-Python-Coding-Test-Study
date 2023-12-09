// https://school.programmers.co.kr/learn/courses/30/lessons/12916?language=javascript
function solution(s) {
  // 자바스크립트 특정 문자열 개수 구하기
  return s.toLowerCase().split("p").length - 1 ===
    s.toLowerCase().split("y").length - 1
    ? true
    : false;
}

console.log(solution("pPoooyY"));
