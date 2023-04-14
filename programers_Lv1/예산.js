function solution(d, budget) {
  var answer = 0;
  let sum = 0;

  d.sort((a, b) => a - b);

  for (let i of d) {
    sum += i;
    if (budget < sum) {
      break;
    }
    answer++;
  }

  return answer;
}

console.log(solution([1, 3, 2, 5, 4], 9));
console.log(solution([2, 2, 3, 3], 10));
