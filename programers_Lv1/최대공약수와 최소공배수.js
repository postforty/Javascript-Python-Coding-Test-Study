// https://school.programmers.co.kr/learn/courses/30/lessons/12940?language=javascript
function solution(n, m) {
  // 최대 공약수 구하기
  const gcdFunc = (a, b) => (a % b === 0 ? b : gcdFunc(b, a % b));
  const gcd = gcdFunc(n, m);

  // 최소 공배수 구하기
  const lcm = Number((n * m) / gcd);

  return [gcd, lcm];
}

console.log(solution(3, 12));
