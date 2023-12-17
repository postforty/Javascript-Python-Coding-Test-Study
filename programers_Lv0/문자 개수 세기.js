// https://school.programmers.co.kr/learn/courses/30/lessons/181902?language=javascript
const alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

function solution(my_string) {
  var answer = [];

  [...alpha].forEach((el) => {
    answer.push(
      [...my_string].reduce((acc, curr) => {
        acc += el === curr ? 1 : 0;
        return acc;
      }, 0)
    );
  });

  return answer;
}

console.log(solution("Programmers"));
