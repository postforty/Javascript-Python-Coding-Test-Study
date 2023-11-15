// https://school.programmers.co.kr/learn/courses/30/lessons/68935?language=javascript
function solution(n) {
  var answer = "";

  while (true) {
    if (n < 3) {
      answer += String(n);
      break;
    }
    answer += String(n % 3);
    n = ~~(n / 3);
  }

  return parseInt(answer, 3);
}

console.log(solution(45));
