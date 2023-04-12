function solution(s) {
  let left = 0;

  if (s[0] === ")" || s[s.length - 1] === "(") {
    return false;
  }

  for (let i of s) {
    if (i === "(") {
      left++;
    } else if (i === ")") {
      if (left) {
        left--;
      } else {
        return false;
      }
    }
  }

  return left !== 0 ? false : true;
}

console.log(solution("())(()")); // 중간에 ")("가 있는 테스트 케이스에 대한 처리 놓치지 말아야!
console.log(solution("(()("));
console.log(solution("()"));
