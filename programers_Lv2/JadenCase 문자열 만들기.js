function solution(s) {
  var answer = [...s].map((el) => el.toLowerCase());

  answer[0] = answer[0].toUpperCase();

  for (let i = 0; i < answer.length; i++) {
    if (answer[i] !== " " && answer[i - 1] === " ") {
      answer[i] = answer[i].toUpperCase();
    }
  }

  return answer.join("");
}

console.log(solution("for the last week"));
