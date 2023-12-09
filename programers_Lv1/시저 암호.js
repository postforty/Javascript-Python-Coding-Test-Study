// https://school.programmers.co.kr/learn/courses/30/lessons/12926?language=javascript
function solution(s, n) {
  const alphaLower = "abcdefghijklmnopqrstuvwxyz";
  const alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  const answer = [...s]
    .map((el) => {
      return alphaLower.includes(el)
        ? alphaLower.indexOf(el) + n >= alphaLower.length
          ? alphaLower[alphaLower.indexOf(el) + n - alphaLower.length]
          : alphaLower[alphaLower.indexOf(el) + n]
        : alphaUpper.includes(el)
        ? alphaUpper.indexOf(el) + n >= alphaUpper.length
          ? alphaUpper[alphaUpper.indexOf(el) + n - alphaUpper.length]
          : alphaUpper[alphaUpper.indexOf(el) + n]
        : el;
    })
    .join("");

  return answer;
}

console.log(solution("a B z", 4));
console.log(solution("z", 1));
