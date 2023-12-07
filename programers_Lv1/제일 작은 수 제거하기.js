// https://school.programmers.co.kr/learn/courses/30/lessons/12935
function solution(arr) {
  const answer = arr.filter((el) => el !== Math.min(...arr));
  return answer.length === 0 ? [-1] : answer;
}

console.log(solution([4, 3, 2, 1]));
