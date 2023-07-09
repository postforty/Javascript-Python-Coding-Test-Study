// https://school.programmers.co.kr/learn/courses/30/lessons/92335
function solution(n, k) {
  let revBase = "";

  let num1 = n;
  while (num1 > 0) {
    let num2 = num1 % k;
    num1 = Math.floor(num1 / k);
    revBase += num2.toString();
  }
  revBase = revBase.split("").reverse().join("");
  const tempArr = revBase.split("0");

  const isPrime = (num) => {
    const start = 3;
    const end = parseInt(num ** 0.5) + 1;

    const range = Array.from(
      { length: end - start },
      (_, index) => index + start
    );

    for (let i of range) {
      if (num % i == 0) {
        return 0;
      }
    }
    return 1;
  };

  let count = 0;
  for (let i of tempArr) {
    let num = i.length != 0 ? Number(i) : 0;
    if (num < 2) {
      continue;
    }
    if (num == 2) {
      count++;
    } else {
      count += isPrime(num);
    }
  }
  return count;
}

console.log(solution(437674, 3));
