// https://school.programmers.co.kr/learn/courses/30/lessons/12918#qna
function solution(s) {
  const numStr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const numStrArr = [...numStr];
  let answer1 = numStrArr.some((el) => s.includes(el)) ? false : true;
  let answer2 = s.length === 4 || s.length === 6;
  return answer1 && answer2;
}

// console.log(solution("0x16"));
console.log(solution("123ABC"));
