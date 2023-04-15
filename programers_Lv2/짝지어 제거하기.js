function solution(s) {
  const rst = [];

  rst[0] = s[0];
  ss = s.substring(1);

  for (let el of ss) {
    if (!rst) {
      rst.push(el);
    } else if (rst[rst.length - 1] !== el) {
      rst.push(el);
    } else if (rst[rst.length - 1] === el) {
      rst.pop();
    }
  }

  return rst.length === 0 ? 1 : 0;
}

console.log(solution("baabaa"));
console.log(solution("cdcd"));
