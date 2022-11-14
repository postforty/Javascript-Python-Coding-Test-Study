function solution(numlist, n) {
  var answer = [];
  answer = numlist.sort((a, b) => {
    let num1 = Math.abs(a - n);
    let num2 = Math.abs(b - n);
    if (num1 === num2) return b - a;
    return num1 - num2;
  });
  return answer;
}
console.log(solution([1, 2, 3, 4, 5, 6], 4));
