// 테스트 1, 2, 6, 7 실패
function solution(numbers, k) {
  var answer = 0;
  let idx = 0;
  for (let i = 0; i < k; i++) {
    if (idx > numbers.length) {
      idx %= numbers.length;
    }
    answer = numbers[idx];
    idx += 2;
  }
  return answer;
}
console.log(solution([1, 2, 3], 3));
