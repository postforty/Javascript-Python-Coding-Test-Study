// https://school.programmers.co.kr/learn/courses/30/lessons/12930?language=javascript
function solution(s) {
  const sArr = s.split(" ");
  const answer = sArr
    .map((el) =>
      [...el]
        .map((v, i) => (i % 2 === 0 ? v.toUpperCase() : v.toLowerCase()))
        .join("")
    )
    .join(" ");

  return answer;
}

console.log(solution("try hello world"));
console.log(solution("a  b  c"));
