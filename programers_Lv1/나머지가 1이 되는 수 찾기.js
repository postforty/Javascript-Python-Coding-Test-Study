function solution(n) {
  // 파이썬의 range(1, n)과 같은 코드
  arrNums = Array.from({ length: n - 1 }, (_, index) => index + 1);
  for (let num of arrNums) {
    if (n % num === 1) {
      return num;
    }
  }
}

console.log(solution(10));
