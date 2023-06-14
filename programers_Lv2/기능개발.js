// https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3
function solution(progresses, speeds) {
  var answer = [];

  const daysArr = [];
  progresses.forEach((v, i) => {
    let goal = v;
    let days = 0;
    while (goal < 100) {
      goal += speeds[i];
      days++;
    }
    daysArr.push(days);
  });

  let start = daysArr[0];
  let cnt = 1;
  daysArr.slice(1).forEach((v) => {
    if (start >= v) {
      cnt++;
    } else {
      answer.push(cnt);
      cnt = 1;
      start = v;
    }
  });
  answer.push(cnt);

  return answer;
}

console.log(solution([93, 30, 55], [1, 30, 5])); // [2, 1]
