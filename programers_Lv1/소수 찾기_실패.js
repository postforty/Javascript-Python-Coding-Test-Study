// https://school.programmers.co.kr/learn/courses/30/lessons/12921
// 효율성 테스트 1, 2, 4 실패(시간 초과)
function solution(n) {
  const isPrimeNum = (n) => {
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  };

  let answer = 0;
  for (let i = 2; i <= n; i++) {
    if ((i !== 2 && i % 2 === 0) || (i !== 3 && i % 3 === 0)) {
      continue;
    }
    isPrimeNum(i) && answer++;
  }

  return answer;
}

console.log(solution(10));
