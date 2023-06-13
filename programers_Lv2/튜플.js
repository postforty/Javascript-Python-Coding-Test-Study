function solution(s) {
  const sSplit = s.split(",");
  const sNums = sSplit.map((v) => +v.match(/\d+/g)[0]);
  const sObj = sNums.reduce((acc, cur) => {
    acc[cur] = acc[cur] ? acc[cur] + 1 : 1;
    return acc;
  }, {});
  const sArr = Object.entries(sObj).sort((a, b) => b[1] - a[1]);
  const answer = sArr.map((v) => +v[0]);

  return answer;
}

console.log(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")); // [3, 2, 4, 1]
