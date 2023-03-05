function solution(n) {
  var answer = 0;
  const tempArr = [];
  let count = 1;
  while (tempArr.length !== 100) {
    if (
      count % 3 === 0 ||
      count % 10 === 3 ||
      (count / 10 >= 3 && count / 10 < 4) ||
      ((count - 100) / 10 >= 3 && (count - 100) / 10 < 4)
    ) {
      count += 1;
      continue;
    }
    tempArr.push(count);
    count += 1;
  }
  answer = tempArr[n - 1];
  return answer;
}

console.log(solution(15));
