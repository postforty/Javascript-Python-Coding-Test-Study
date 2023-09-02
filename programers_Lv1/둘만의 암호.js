// https://school.programmers.co.kr/learn/courses/30/lessons/155652?language=javascript
function solution(s, skip, index) {
  var answer = "";

  const alpha = "abcdefghijklmnopqrstuvwxyz";
  let newAlpha = "";

  for (let i in alpha) {
    if (skip.includes(alpha[i])) {
      continue;
    }
    newAlpha += alpha[i];
  }

  const newAlphaLength = newAlpha.length;

  for (let v of s) {
    let idx =
      newAlpha.indexOf(v) + index >= newAlphaLength
        ? (newAlpha.indexOf(v) + index) % newAlphaLength
        : newAlpha.indexOf(v) + index;

    answer += newAlpha[idx];
  }

  return answer;
}

console.log(solution("aukks", "wbqd", 5)); // "happy"
