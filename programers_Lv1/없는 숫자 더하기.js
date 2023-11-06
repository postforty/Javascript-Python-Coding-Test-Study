// https://school.programmers.co.kr/learn/courses/30/lessons/86051?language=javascript
function solution(numbers) {
  const arr = [];
  arr.length = 10;
  arr.fill(0);
  const resultArr = [...Object.keys(arr)];

  const result = resultArr.reduce((acc, curr) => {
    curr = curr;
    if (!numbers.includes(~~curr)) {
      acc = acc + ~~curr;
    }
    return acc;
  }, 0);
  return result;
}

console.log(solution([1, 2, 3, 4, 6, 7, 8, 0]));
