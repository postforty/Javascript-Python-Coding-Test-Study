// https://school.programmers.co.kr/learn/courses/30/lessons/134240?language=javascript
function solution(food) {
  let answer = food
    .reduce((acc, curr, idx) => {
      acc += idx.toString().repeat(Math.floor(curr / 2));
      return acc;
    }, 0)
    .slice(1);
  console.log(answer);
  // 문자열 뒤집기
  return answer + "0" + answer.split("").reverse().join("");
}

console.log(solution([1, 3, 4, 6])); // 1223330333221
