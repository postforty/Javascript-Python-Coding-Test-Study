// https://school.programmers.co.kr/learn/courses/30/lessons/82612?language=javascript
function solution(price, money, count) {
  var answer = 0;

  const countArr = Array.from({ length: count }, (_, i) => i + 1);

  const total = countArr.reduce((acc, curr) => {
    temp = price * curr;
    return acc + temp;
  }, 0);

  answer = money - total;

  return answer < 0 ? -answer : 0;
}

console.log(solution(3, 20, 4)); // 10
