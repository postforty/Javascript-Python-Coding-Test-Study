// https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=javascript
function solution(arr) {
  let temp = -1;
  const answer = [];
  arr.forEach((el) => {
    if (el !== temp) {
      temp = el;
      answer.push(el);
    }
  });

  return answer;
}

console.log(solution([1, 1, 3, 3, 0, 1, 1]));
