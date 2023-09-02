// https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=javascript
function solution(t, p) {
  var answer = 0;
  const numLength = p.length;
  let i = 0;

  while (1) {
    num = t.slice(i, numLength + i);
    if (num.length !== numLength) {
      break;
    }
    answer += +num <= +p ? 1 : 0;
    i++;
  }

  return answer;
}

console.log(solution("500220839878", "7")); // 8
