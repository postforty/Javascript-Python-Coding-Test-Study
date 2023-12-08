// https://school.programmers.co.kr/learn/courses/30/lessons/12928
function solution(n) {
  const arrNumber = Array.from({ length: n }, (v, i) => i + 1);
  return arrNumber.reduce((acc, curr) => {
    acc += n % curr === 0 ? curr : 0;
    return acc;
  }, 0);
}

console.log(solution(12));
