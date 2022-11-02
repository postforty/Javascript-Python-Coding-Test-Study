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
    // let idx = numbers.indexOf(str[i]);
    // if (idx > -1) {
    //   temp[idx] = i;
    // }
    numbers = numbers.split(str[i]).join(i);
  }
  answer = parseInt(numbers);
  return answer;
}
console.log(solution("onefourzerosixseven"));
