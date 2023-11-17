// https://school.programmers.co.kr/learn/courses/30/lessons/17682?language=javascript
function solution(dartResult) {
  const areas = {
    S: "**1",
    D: "**2",
    T: "**3",
  };

  const opts = {
    "~": "*2",
    "#": "*(-1)",
  };

  const areasArr = ["S", "D", "T"];
  const optsArr = ["~", "#"];
  const numArr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

  const tempDart = dartResult.replaceAll("10", ",@");

  const tempDart2 = numArr.reduce((acc, curr) => {
    return acc.replaceAll(curr, `,${curr}`);
  }, tempDart);

  const tempDartArr = tempDart2.split(",");

  tempDartArr.forEach((v, i) => {
    if (v.includes("*")) {
      tempDartArr[i] = v.replace("*", "") + "~";
      tempDartArr[i - 1] = tempDartArr[i - 1] + "~";
    }
  });

  dartResult = tempDartArr.slice(1, tempDartArr.length).join("");

  numArr.forEach((v, i) => {
    dartResult = dartResult.replaceAll(v, `+${v}`);
  });

  optsArr.forEach((v, i) => {
    dartResult = dartResult.replaceAll(v, opts[v]);
  });

  areasArr.forEach((v, i) => {
    dartResult = dartResult.replaceAll(v, areas[v]);
  });

  dartResult = dartResult.replaceAll("@", "+10");

  return eval(dartResult.slice(1, dartResult.length));
}

console.log(solution("1D2S#10S")); // 9
