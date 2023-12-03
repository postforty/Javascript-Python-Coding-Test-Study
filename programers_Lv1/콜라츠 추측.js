// https://school.programmers.co.kr/learn/courses/30/lessons/12943?language=javascript
function solution(num) {
  var count = 0;
  while (1) {
    if (num === 1) {
      return count;
    }
    if (count >= 500) {
      return -1;
    }
    if (num % 2 == 0) {
      num /= 2;
    } else {
      num *= 3;
      num++;
    }
    count++;
  }
}

console.log(solution(6));
