function solution(score) {
  var answer = [];
  let temp = [];
  for (let arr of score) {
    temp.push((arr[0] + arr[1]) / 2);
  }
  answer = Array.from({ length: temp.length }, () => 1);
  for (let i = 0; i < answer.length; i++) {
    for (let j = 0; j < answer.length; j++) {
      if (temp[j] > temp[i]) answer[i]++; // 비교해서 작을 수록 1씩 증가
    }
  }
  return answer;
}
console.log(
  solution([
    [80, 70],
    [70, 80],
    [30, 50],
    [90, 100],
    [100, 90],
    [100, 100],
    [10, 30],
  ])
);
