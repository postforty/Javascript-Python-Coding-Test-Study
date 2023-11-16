// https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=javascript
function solution(answers) {
  const studentsInfo = [
    { pick: [1, 2, 3, 4, 5], pickLength: 5 },
    {
      pick: [2, 1, 2, 3, 2, 4, 2, 5],
      pickLength: 8,
    },
    { pick: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], pickLength: 10 },
  ];

  const answersLength = answers.length;

  studentsInfo.forEach((v, i) => {
    if (answersLength > v.pickLength) {
      studentsInfo[i].pick = Array.from(
        {
          length:
            answersLength % studentsInfo[i].pickLength === 0
              ? answersLength / studentsInfo[i].pickLength
              : Number(answersLength / studentsInfo[i].pickLength) + 1,
        },
        () => studentsInfo[i].pick
      ).flat();
    }
  });

  const scoreArr = [0, 0, 0];

  const [student1, student2, student3] = studentsInfo;
  const pickArr = [student1.pick, student2.pick, student3.pick];
  answers.forEach((v, i) => {
    pickArr.forEach((w, j) => {
      if (v === w[i]) {
        scoreArr[j]++;
      }
    });
  });

  let maxScore = Math.max(...scoreArr);

  return scoreArr
    .map((el, i) => (el === maxScore ? i + 1 : -1))
    .filter((index) => index !== -1);
}

console.log(solution([1, 3, 2, 4, 2]));
