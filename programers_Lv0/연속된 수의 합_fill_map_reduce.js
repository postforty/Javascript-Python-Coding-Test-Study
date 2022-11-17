// 주석의 코드는 테스트 10을 통과하지 못했음
// function solution(num, total) {
//   let mid = Math.round(total / num);
//   var answer = [mid];
//   for (let i = 1; i <= Math.floor(num / 2); i++) {
//     if (answer.reduce((a, b) => a + b) + (mid - i) <= total) {
//       answer.unshift(mid - i);
//     }
//     if (answer.reduce((a, b) => a + b) + (mid + i) <= total) {
//       answer.push(mid + i);
//     }
//   }
//   if (answer.reduce((a, b) => a + b) !== total) {
//     while (true) {}
//   } else {
//     return answer;
//   }
// }

// 첫 시작하는 숫자를 찾아내 배열의 총합이 total과 같을때까지 배열의 요소를 증가 시킴
function solution(num, total) {
  // var answer = [];
  let startNum = 0;
  let twoPointer = new Array(num)
    .fill(0)
    .map((a, b) => a + b)
    .reduce((a, b) => a + b, 0);
  while (twoPointer !== total) {
    if (twoPointer < total) {
      startNum++;
    } else {
      startNum--;
    }
    twoPointer = new Array(num)
      .fill(0)
      .map((a, b) => b + startNum)
      .reduce((a, b) => a + b);
  }
  // answer = [startNum];
  // let n = startNum;
  // while (total !== answer.reduce((a, b) => a + b)) {
  //   n++;
  //   answer.push(n);
  // }
  // return answer;

  // 위 주석의 코드를 map을 이용해 간단히 하였음
  return new Array(num).fill(0).map((a, b) => b + startNum);
}

console.log(solution(5, 5));
