function solution(array, n) {
  // for문 사용 코드 제출시 테스트 5 실패하였음
  const answer = array
    .filter(
      (a) => Math.abs(a - n) === Math.min(...array.map((a) => Math.abs(a - n)))
    )
    .sort((a, b) => a - b)[0];
  return answer;
}
console.log(solution([3, 10, 28], 20));
