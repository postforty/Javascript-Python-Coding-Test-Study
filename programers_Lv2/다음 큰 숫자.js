function solution(n) {
  var answer = 0;
  nCnt = [...n.toString(2)].filter((el) => el === "1").length;

  while (true) {
    n++;
    tempCnt = [...n.toString(2)].filter((el) => el === "1").length;
    if (tempCnt === nCnt) {
      answer = n;
      break;
    }
  }

  return answer;
}

console.log(solution(15));
