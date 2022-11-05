function solution(s) {
  var answer = 0;
  s = s.split(" ");
  while (s.includes("Z")) {
    s.splice(s.indexOf("Z") - 1, 2); // splice의 용법 주의
  }
  answer = s.reduce((a, b) => a + Number(b), 0);
  return answer;
}
console.log(solution("10 Z 20 Z 1"));
