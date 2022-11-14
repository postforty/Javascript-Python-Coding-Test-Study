function solution(quiz) {
  var answer = [];
  let rst = "";

  for (let i of quiz) {
    let [a, b] = i.split(" = ");
    let rstA = eval(a);
    rst += parseInt(rstA) === parseInt(b) ? "O" : "X";
    answer = [...rst];
  }

  return answer;
}

console.log(
  solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"])
);
