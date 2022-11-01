function solution(balls, share) {
  var answer = 0;
  answer = factorial(balls) / (factorial(balls - share) * factorial(share));
  return answer;
}
// factorial 계산 시 number로 계산을 하면 큰 수로 연산을 하게 될 경우 정확한 값이 출력되지 않는 현상이 발생한다.
// factorial 계산 시 매우 큰 수가 연산될 수 있기 때문에 2^53 - 1까지 안전하게 다룰 수 있는 BigInt 활용
function factorial(num) {
  let ret = BigInt(1);
  for (let i = 2; i <= num; i++) {
    ret *= BigInt(i);
  }
  return ret;
}
console.log(solution(5, 3));
