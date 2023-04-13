function solution(n) {
  var answer = 0;
  for (let i = 1; i < n + 1; i++) {
    let temp = 0;
    for (let j = i; j < n + 1; j++) {
      if (temp < n + 1) {
        temp += j;
      }
      if (temp == n) {
        answer++;
        continue;
      }
      if (temp > n) {
        break;
      }
    }
  }
  return answer;
}

console.log(solution(15));
