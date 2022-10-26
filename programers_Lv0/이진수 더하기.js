// 테스트 1, 4, 5 실패
// function solution(bin1, bin2) {
//   var answer = [];
//   let temp = [];
//   let bin1Arr = bin1.split("");
//   let bin2Arr = bin2.split("");
//   while (temp.length > 0 || bin1Arr.length > 0 || bin2Arr.length > 0) {
//     let add =
//       (bin1Arr.length > 0 ? Number(bin1Arr.pop()) : 0) +
//       (bin2Arr.length > 0 ? Number(bin2Arr.pop()) : 0) +
//       (temp.length > 0 ? temp.pop() : 0);
//     if (add === 3) {
//       temp.unshift(1);
//       answer.unshift(1);
//     } else if (add === 2) {
//       temp.unshift(1);
//       answer.unshift(0);
//     } else {
//       answer.unshift(1);
//     }
//   }
//   return answer.join("");
// }
// console.log(solution("1", "1111"));

// 10진수를 다른 진수로 변환하기 위해서는 toString()을,
// 다른 진수를 10진수로 변환하기 위해서는 parseInt()를 쓴다.
function solution(bin1, bin2) {
  var answer = "";
  let add = (parseInt(bin1, 2) + parseInt(bin2, 2)).toString(2);
  answer = add;
  return answer;
}
console.log(solution("1001", "1111"));
