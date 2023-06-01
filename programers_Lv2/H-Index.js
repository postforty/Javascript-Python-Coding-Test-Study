function solution(citations) {
  const sortedArr = citations.sort((a, b) => b - a);
  const num = sortedArr[0];
  for (let i = num; i >= 0; i--) {
    let cnt = 0;
    for (let j of sortedArr) {
      if (j >= i) {
        cnt++;
        if (i === cnt) {
          return cnt;
        }
      }
    }
  }
  return 0;
}

console.log(solution([3, 0, 6, 1, 5])); // 3
console.log(solution([25, 8, 5, 3, 3])); // 3
