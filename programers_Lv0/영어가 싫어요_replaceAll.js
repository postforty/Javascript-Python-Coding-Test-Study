function solution(numbers) {
  var answer = "";
  const str = [
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
  const temp = {};
  for (let i = 0; i < str.length; i++) {
    numbers = numbers.replaceAll(str[i], i); // 동일 숫자의 경우로 인해 replace로는 안됨
  }
  answer = parseInt(numbers);
  return answer;
}
console.log(solution("onefourzerosixseven"));
