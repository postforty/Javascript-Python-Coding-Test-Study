// https://school.programmers.co.kr/learn/courses/30/lessons/77884?language=javascript
function solution(left, right) {
  var answer = 0;

  const countDivisor = (number) => {
    const numberArr = Array.from({ length: number }, (_, i) => i + 1);
    const count = numberArr.reduce((acc, curr) => {
      acc += number % curr === 0 ? 1 : 0;
      return acc;
    }, 0);
    return count;
  };

  for (let i = left; i <= right; i++) {
    answer += countDivisor(i) % 2 === 0 ? i : -i;
  }

  return answer;
}

console.log(solution(13, 17));
