// https://school.programmers.co.kr/learn/courses/30/lessons/12903?language=javascript
function solution(s) {
  var answer =
    s.length % 2 === 0
      ? s.slice(Math.floor(s.length / 2) - 1, Math.floor(s.length / 2) + 1)
      : s.slice(Math.floor(s.length / 2), Math.floor(s.length / 2) + 1);
  return answer;
}

console.log(solution("abcde"));
console.log(solution("qwer"));
