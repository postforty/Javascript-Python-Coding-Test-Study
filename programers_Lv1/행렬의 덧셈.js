// https://school.programmers.co.kr/learn/courses/30/lessons/12950?language=javascript
function solution(arr1, arr2) {
  var answer = [];
  arr1.forEach((v, i) => {
    let tempArr = [];
    v.forEach((w, j) => {
      tempArr.push(w + arr2[i][j]);
    });
    answer.push(tempArr);
  });
  return answer;
}

console.log(
  solution(
    [
      [1, 2],
      [2, 3],
    ],
    [
      [3, 4],
      [5, 6],
    ]
  )
);
