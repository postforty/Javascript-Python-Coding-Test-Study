// https://school.programmers.co.kr/learn/courses/30/lessons/133499?language=javascript
function solution(babbling) {
  var answer = 0;

  for (let str of babbling) {
    if (
      str.includes("ayaaya") ||
      str.includes("yeye") ||
      str.includes("woowoo") ||
      str.includes("mama")
    ) {
      continue;
    }

    const result = str
      .replaceAll("aya", "_")
      .replaceAll("ye", "_")
      .replaceAll("woo", "_")
      .replaceAll("ma", "_")
      .replaceAll("_", "");

    if (!result) {
      answer++;
    }
  }
  return answer;
}

console.log(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])); // 2
