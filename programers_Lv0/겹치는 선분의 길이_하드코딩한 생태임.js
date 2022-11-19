// 겹치는 선분의 길이
function solution(lines) {
  var answer = 0;

  // 범위 의 최대값 최소값 구하기
  let min = 0;
  let max = 0;
  for (let i = 0; i < lines.length; i++) {
    if (min > lines[i][0]) {
      min = lines[i][0];
    }
  }
  for (let i = 0; i < lines.length; i++) {
    if (max < lines[i][1]) {
      max = lines[i][1];
    }
  }

  // 최대값 최소값 이용해 전체 길이의 선분 만들기
  const range = [];
  for (let i = min; i <= max; i++) {
    range.push(i);
  }

  // 전체 길이 선분의 비교 대상 배열. 선분이 존재하는 경우 "-", 겹치는 경우 "+"로 요소를 변경하는 배열
  const resultArr = new Array(range.length).fill(0);

  for (let i = 0; i < lines.length; i++) {
    for (let j = lines[i][0]; j < lines[i][1]; j++) {
      let idx = range.indexOf(j);
      if (resultArr[idx] === "-") resultArr[idx] = "+";
      else if (resultArr[idx] === "+") resultArr[idx] = "+";
      else resultArr[idx] = "-";
    }
  }

  // 겹치는 선분에 해당하는 "+" 카운트
  let rst = resultArr.reduce((a, b) => {
    a[b] = (a[b] || 0) + 1;
    return a;
  }, {})["+"];

  // "+"가 undefined인 경우 0처리
  answer = rst !== undefined ? rst : 0;
  return answer;
}

console.log(
  solution([
    [-1, 1],
    [1, 3],
    [3, 9],
  ])
);
