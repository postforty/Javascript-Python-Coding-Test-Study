function solution(balls, share) {
  var answer = 0;
  answer = factorial(balls) / (factorial(balls - share) * factorial(share));
  return answer;
}
function factorial(num) {
  let ret = 1;
  for (let i = 2; i <= num; i++) {
    ret *= i;
  }
  return ret;
}
console.log(solution(5, 3));
