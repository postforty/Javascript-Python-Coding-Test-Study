function solution(my_string) {
  var answer = 0;
  answer = eval(my_string); // 문자열 연산자를 일반 연산자로 바꾸어 계산
  return answer;
}
console.log(solution("3 + 4"));
