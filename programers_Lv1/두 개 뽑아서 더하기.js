// https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=javascript
function solution(numbers) {
  var answer = [];

  function combinations(arr, k) {
    const result = [];

    function backtrack(subset, start) {
      if (subset.length === k) {
        result.push([...subset]);
        return;
      }

      for (let i = start; i < arr.length; i++) {
        subset.push(arr[i]);
        backtrack(subset, i + 1);
        subset.pop();
      }
    }

    backtrack([], 0);
    return result;
  }

  combinations(numbers, 2).forEach((e) => {
    const [a, b] = e;
    answer.push(a + b);
  });

  return Array.from(new Set(answer)).sort((a, b) => a - b);
}

console.log(solution([2, 1, 3, 4, 1]));
