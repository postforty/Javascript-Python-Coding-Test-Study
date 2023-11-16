// https://school.programmers.co.kr/learn/courses/30/lessons/42748?language=javascript
function solution(array, commands) {
  var answer = [];

  commands.forEach((arr) => {
    const [a, b, c] = arr;
    const tempArr = array.slice(a - 1, b).sort((a, b) => a - b);
    answer.push(tempArr[c - 1]);
  });

  return answer;
}

console.log(
  solution(
    [1, 5, 2, 6, 3, 7, 4],
    [
      [2, 5, 3],
      [4, 4, 1],
      [1, 7, 3],
    ]
  )
);
