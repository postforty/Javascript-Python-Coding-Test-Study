function solution(n) {
  const answer = [0, 1];

  if (n === 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  }

  for (let i = 0; i < n - 1; i++) {
    const temp = (answer[0] + answer[1]) % 1234567;
    answer[0] = answer[1];
    answer[1] = temp;
  }

  return answer[1];
}

console.log(solution(100));
