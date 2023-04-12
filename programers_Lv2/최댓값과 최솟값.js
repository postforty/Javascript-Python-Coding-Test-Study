function solution(s) {
  var answer = "";

  const arr = s.split(" ").map((el) => parseInt(el));

  let minVal = arr.sort((a, b) => a - b)[0];
  let maxVal = arr.sort((a, b) => b - a)[0];

  answer = `${minVal} ${maxVal}`;

  return answer;
}

console.log(solution("1 2 3 4"));
