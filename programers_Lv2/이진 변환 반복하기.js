function solution(s) {
  const answer = [];

  let tempS = s;
  let count = 0;
  let zero = 0;

  while (tempS !== "1") {
    zero += [...tempS].filter((el) => el === "0").length;
    let rmZero = [...tempS].filter((el) => el === "1").join("");
    tempS = rmZero.length.toString(2);
    count++;
  }

  answer.push(count);
  answer.push(zero);

  return answer;
}

console.log(solution("110010101001"));
console.log(solution("1111111"));
console.log(solution("01110"));
