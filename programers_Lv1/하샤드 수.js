// https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=javascript
function solution(x) {
  return (
    x %
      String(x)
        .split("")
        .reduce((acc, curr) => {
          acc += Number(curr);
          return acc;
        }, 0) ===
    0
  );
}

console.log(solution(10));
