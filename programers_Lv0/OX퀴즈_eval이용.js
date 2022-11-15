function solution(quiz) {
  var answer = [];
  let rst = "";

  for (let i of quiz) {
    let [a, b] = i.split(" = "); // 공백 제거를 위해 replaceAll(' ', '') 코드를 넣었는데 런타임 에러가 발생하여 생략하였으나 eval은 공백 여부와 상관없이 작동하였음
    let rstA = eval(a);
    rst += parseInt(rstA) === parseInt(b) ? "O" : "X";
    answer = [...rst];
  }

  return answer;
}

console.log(
  solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"])
);
