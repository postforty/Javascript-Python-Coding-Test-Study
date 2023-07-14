function solution(msg) {
  var answer = [];
  let newNum = 27;
  const alpaStr = new Array(26)
    .fill()
    .map((_, i) => String.fromCharCode(i + 65))
    .join("");
  const alpaObj = alpaStr.split("").reduce((acc, curr, idx) => {
    return { ...acc, [curr]: idx + 1 };
  }, {});

  let newMsg = msg;
  let tempStr = "";

  while (newMsg.length > 0) {
    tempStr += newMsg.slice(0, 1);
    if (alpaObj[tempStr] !== undefined) {
      newMsg = newMsg.slice(1, newMsg.length);
      continue;
    } else {
      alpaObj[tempStr] = newNum;
      newNum++;
      answer.push(alpaObj[tempStr.slice(0, -1)]);
      tempStr = "";
    }
  }
  answer.push(alpaObj[tempStr]);
  return answer;
}

console.log(solution("KAKAO")); // [11, 1, 27, 15]
