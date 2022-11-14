function solution(chicken) {
  let coupon = chicken;
  var answer = 0;
  while (coupon >= 10) {
    answer += Math.floor(coupon / 10);
    coupon = Math.floor((coupon % 10) + coupon / 10);
  }
  return answer;
}
console.log(solution(1081));
