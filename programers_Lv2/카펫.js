function solution(brown, yellow) {
  let total = brown + yellow;

  const rst = [];

  for (let i = total; i > 0; i--) {
    if (total % i == 0) {
      rst.push(i);
    }
  }

  let rst_r = rst.slice().sort((a, b) => a - b);

  const answer = [];
  for (let i in rst) {
    if ((rst[i] - 2) * (rst_r[i] - 2) === yellow) {
      answer.push(rst[i]);
      answer.push(rst_r[i]);
      break;
    }
  }

  return answer;
}

console.log(solution(18, 6)); // [8, 3]
