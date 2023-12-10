// https://school.programmers.co.kr/learn/courses/30/lessons/12915?language=javascript
function solution(strings, n) {
  // 자바스크립트 특정 문자 기준 정렬
  var answer = strings.sort().sort((a, b) => a.charCodeAt(n) - b.charCodeAt(n));
  return answer;
}

console.log(solution(["sun", "bed", "car"], 1));
