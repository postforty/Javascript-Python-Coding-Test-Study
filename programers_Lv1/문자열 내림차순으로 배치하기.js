// https://school.programmers.co.kr/learn/courses/30/lessons/12917?language=javascript
function solution(s) {
  alphaLower = [..."abcdefghijklmnopqrstuvwxyz"];

  console.log(alphaLower);

  const sArr = [...s];

  const first = [];
  const second = [];

  sArr.forEach((el) => {
    if (alphaLower.includes(el)) {
      first.push(el);
    } else {
      second.push(el);
    }
  });

  return first.sort().reverse().join("") + second.sort().reverse().join("");
}

console.log(solution("Zbcdefg"));
