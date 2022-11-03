function solution(my_string) {
  var answer = 0;
  answer = eval(my_string.replace(" ", ""));
  return answer;
}
console.log(solution("3 + 4"));
