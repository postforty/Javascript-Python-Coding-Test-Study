function solution(my_string) {
  var answer = 0;
  const strArr = my_string.split("");
  for (let i = 0; i < my_string.length; i++) {
    let el = "";
    // isNaN 이용해 NaN 값을 제외
    while (!isNaN(Number(my_string[i]))) {
      el += my_string[i];
      i++;
    }
    answer += Number(el);
  }
  return answer;
}
console.log(solution("aAb1B2cC34oOp"));
