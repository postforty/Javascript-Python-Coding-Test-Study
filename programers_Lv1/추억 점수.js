// https://school.programmers.co.kr/learn/courses/30/lessons/176963?language=javascript
function solution(name, yearning, photo) {
  var answer = [];
  const scoreBoard = name.reduce((acc, curr, idx) => {
    acc[curr] = yearning[idx];
    return acc;
  }, {});
  answer = photo.map((arr) => {
    const sum = arr.reduce((acc, curr) => {
      return acc + (scoreBoard[curr] ?? 0);
    }, 0);
    return sum;
  });
  return answer;
}

console.log(
  solution(
    ["may", "kein", "kain", "radi"],
    [5, 10, 1, 3],
    [
      ["may", "kein", "kain", "radi"],
      ["may", "kein", "brin", "deny"],
      ["kon", "kain", "may", "coni"],
    ]
  )
); // [19, 15, 6];
