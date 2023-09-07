// https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=javascript
// 1차 시도 : 파이썬 코드와 동일하나 제출시 실패(실패 이유를 모르겠음ㅠ)
// function solution(number, limit, power) {
//   var answer = 0;

//   for (let n = 1; n <= number; n++) {
//     let count = 0;
//     for (let i = 1; i <= Math.floor(Math.sqrt(n)); i++) {
//       n % i === 0 && count++;
//       if (i !== Math.floor(n / i)) {
//         count++;
//       }
//     }
//     if (count > limit) {
//       count = power;
//     }
//     answer += count;
//   }
//   return answer;
// }

// 1~n의 약수찾기 === 1~Math.sqrt(n) 미만의 약수 * 2 + Math.sqrt(n)이 Number라면 1 추가( ex) 4*4=16)

// 프로그래머스 질문하기에 올라온 코드 : 성공
// function solution(number, limit, power) {
//   const numberArray = Array(number)
//     .fill(0)
//     .map((_, idx) => idx + 1);
//   const answer = numberArray
//     .map((number) => {
//       let divideCount = 0;
//       for (let i = 1; i < Math.sqrt(number); i++) {
//         number % i === 0 && divideCount++;
//       }
//       divideCount = divideCount * 2 + Number.isInteger(Math.sqrt(number));
//       return divideCount > limit ? power : divideCount;
//     })
//     .reduce((acc, val) => acc + val, 0);
//   return answer;
// }

// 성공!!!
function solution(number, limit, power) {
  var answer = 0;

  for (let n = 1; n <= number; n++) {
    let divisorSet = new Set();
    for (let i = 1; i <= Math.floor(Math.sqrt(n)); i++) {
      if (n % i === 0) {
        divisorSet.add(i);
        divisorSet.add(Math.floor(n / i));
      }
    }
    answer +=
      Array.from(divisorSet).length > limit
        ? power
        : Array.from(divisorSet).length;
  }
  return answer;
}

console.log(solution(10, 3, 2)); // 21
