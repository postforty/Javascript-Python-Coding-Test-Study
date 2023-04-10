function solution(n, lost, reserve) {
  var answer = n - lost.length;

  const sortedLost = lost.sort((a, b) => a - b);
  const sortedReserve = reserve.sort((a, b) => a - b);

  const sortedLostRemove = [...sortedLost];
  const sortedReserveRemove = [...sortedReserve];

  sortedLost.forEach((value, idx) => {
    if (sortedReserve.indexOf(value) > -1) {
      sortedLostRemove.splice(idx, 1);
      sortedReserveRemove.splice(sortedReserve.indexOf(value), 1);
      answer++;
    }
  });

  const sortedLostRemoveR = [...sortedLost];

  sortedLostRemove.forEach((value) => {
    sortedReserveRemove.indexOf(value - 1) !== -1 && answer++;
    sortedReserveRemove.indexOf(value - 1) !== -1 &&
      sortedReserveRemove.splice(sortedLostRemoveR.indexOf(value), 1);
    sortedReserveRemove.indexOf(value - 1) !== -1 &&
      sortedReserveRemove.splice(sortedReserveRemove.indexOf(value - 1), 1);
  });

  sortedLostRemoveR.forEach((value) => {
    sortedReserveRemove.indexOf(value + 1) !== -1 && answer++;
    sortedReserveRemove.indexOf(value + 1) !== -1 &&
      sortedReserveRemove.splice(sortedReserveRemove.indexOf(value + 1), 1);
  });

  return answer;
}

console.log(solution(5, [2, 4], [1, 3, 5]));
// console.log(solution(5, [2, 4], [3]));
// console.log(solution(3, [3], [1]));
// console.log(solution(5, [4, 2], [3, 5]));
// console.log(solution(4, [2, 3], [3, 4]));
// console.log(solution(4, [3, 2], [3, 4, 2]));
