// https://school.programmers.co.kr/learn/courses/30/lessons/17687?language=python3
function solution(n, t, m, p) {
  const numArr = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
  ];

  const newNumArr = numArr.slice(0, n);

  let resultStr = "0";
  let end = p + (t - 1) * m;
  for (let i = 1; i < end; i++) {
    let num = "";
    let quotient = i;

    while (quotient > 0) {
      let remainder = quotient % n;
      num = newNumArr[remainder] + num;
      quotient = Math.floor(quotient / n);
    }

    resultStr += num;
  }

  const result = Array.from(resultStr.slice(p - 1, -1))
    .filter((_, index) => index % m === 0)
    .join("");

  return result.slice(0, t);
}

// console.log(solution(2, 4, 2, 1)); // "0111"
console.log(solution(16, 16, 2, 2)); // "13579BDF01234567"
