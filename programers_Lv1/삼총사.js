// https://school.programmers.co.kr/learn/courses/30/lessons/131705?language=javascript
function solution(number) {
  var answer = 0;

  //   순열 사용자 정의 함수
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

  const result = combinations(number, 3);

  result.forEach((el) => {
    answer += el.reduce((acc, curr) => acc + curr, 0) == 0 ? 1 : 0;
  });

  return answer;
}

console.log(solution([-2, 3, 0, 2, -5]));
