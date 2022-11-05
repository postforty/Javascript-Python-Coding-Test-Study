function solution(a, b) {
  var answer = 0;
  // 최대공약수 구하기
  const gcdMachine = (a, b) => {
    if (b === 0) return a;
    return gcdMachine(b, a % b);
  };
  let gcd = gcdMachine(a, b);

  // 기약분수 구하기
  b = b / gcd;
  while (b % 5 === 0 || b % 2 === 0) {
    if (b % 5 === 0) {
      b = b / 5;
    } else if (b % 2 === 0) {
      b = b / 2;
    }
  }

  return (answer = b !== 1 ? 2 : b);
}
console.log(solution(7, 20));
