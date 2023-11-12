// https://school.programmers.co.kr/learn/courses/30/lessons/76501?language=javascript
function solution(absolutes, signs) {
  const answer = signs.reduce((acc, curr, idx) => {
    acc += curr ? absolutes[idx] : -absolutes[idx];
    return acc;
  }, 0);

  return answer;
}

console.log(solution([4, 7, 12], [true, false, true]));
