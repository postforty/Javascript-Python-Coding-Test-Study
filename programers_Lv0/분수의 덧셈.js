function solution(numer1, denom1, numer2, denom2) {
  var answer = [];

  let numer = numer1 * denom2 + numer2 * denom1; // 분자
  let denom = denom1 * denom2; // 분모

  // 최대 공약수 구하기
  const gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));

  const g = gcd(denom, numer);

  answer.push(numer / g);
  answer.push(denom / g);
  return answer;
}

console.log(solution(1, 2, 3, 4));
console.log(solution(9, 2, 1, 3));
