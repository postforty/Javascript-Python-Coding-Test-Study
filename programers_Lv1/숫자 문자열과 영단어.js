// https://school.programmers.co.kr/learn/courses/30/lessons/81301
function solution(s) {
  var answer = s;

  const words = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];

  words.forEach((v, i) => {
    answer = answer.replaceAll(v, i); // replace 사용하면 5, 7, 8 통과 안됨
  });
  return ~~answer;
}

console.log(solution("one4seveneight"));
