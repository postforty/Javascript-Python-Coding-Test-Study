// https://school.programmers.co.kr/learn/courses/30/lessons/12901?language=javascript
function solution(a, b) {
  const weekday = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  // 자바스크립트 요일 확인
  return weekday[new Date(`2016-${a}-${b}`).getDay()];
}

console.log(solution(5, 24));
