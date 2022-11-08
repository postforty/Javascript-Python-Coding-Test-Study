function solution(chicken) {
  let coupon = chicken;
  var answer = 0;
  while (coupon >= 10) {
    answer += Math.floor(coupon / 10); // 실수를 정수로 바꿔야. "<< 0"과 같이 비트 연산자 사용할수도 있음
    coupon = Math.floor((coupon % 10) + coupon / 10);
  }
  return answer;
}
console.log(solution(1081));
