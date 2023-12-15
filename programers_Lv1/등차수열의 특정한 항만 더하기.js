// https://school.programmers.co.kr/learn/courses/30/lessons/181931?language=javascript
function solution(a, d, included) {
  return included
    .map((el, idx) => (el ? a + idx * d : 0))
    .reduce((acc, curr) => {
      return (acc += curr);
    }, 0);
}

console.log(solution(3, 4, [true, false, false, true, true]));
