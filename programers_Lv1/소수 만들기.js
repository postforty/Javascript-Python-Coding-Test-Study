// https://school.programmers.co.kr/learn/courses/30/lessons/12977?language=javascript
function solution(nums) {
  var answer = 0;

  // 소수 판별
  const isPrimeNum = (n) => {
    const range = Array.from({ length: n - 2 }, (_, i) => i + 2);
    const result = range.every((v, i) => {
      return n % v !== 0;
    });
    return result;
  };

  // 조합
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

  const sumCombinations = combinations(nums, 3);

  sumCombinations.forEach((v) => {
    const sumNums = v.reduce((acc, curr) => (acc += curr));
    isPrimeNum(sumNums) && answer++;
  });

  return answer;
}

console.log(solution([1, 2, 3, 4]));
