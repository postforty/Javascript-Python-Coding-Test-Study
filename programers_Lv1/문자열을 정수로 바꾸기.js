// https://school.programmers.co.kr/learn/courses/30/lessons/12925?language=javascript
function solution(s) {
  var prefix =
    s.slice(0, 1) === "+" || s.slice(0, 1) === "-" ? s.slice(0, 1) : "";
  var value = s.slice(0, 1) === "+" || s.slice(0, 1) === "-" ? s.slice(1) : s;

  return ~~(prefix + value);
}

console.log(solution("-1234"));
