function solution(n, lost, reserve) {
  var answer = n - lost.length;

  const sortedLost = lost.sort((a, b) => a - b);
  const sortedLostRemove = [...sortedLost];
  const sortedReserve = reserve.sort((a, b) => a - b);

  sortedLost.forEach((value, idx) => {
    if (sortedReserve.includes(value)) {
      sortedLostRemove.splice(idx, 1);
      sortedReserve.splice(idx, 1);
      answer++;
    }
  });
  console.log(sortedReserve);

  sortedLostRemove.forEach((value, idx) => {
    if (sortedReserve.includes(value - 1)) {
      sortedLostRemove.splice(idx, 1);
      sortedReserve.splice(idx);
      answer++;
    }
  });
  console.log(sortedReserve);

  sortedLostRemove.forEach((value, idx) => {
    if (sortedReserve.includes(value + 1)) {
      sortedReserve.splice(idx);
      answer++;
    }
  });
  console.log(sortedReserve);

  return answer;
}

console.log(solution(5, [2, 4], [1, 3, 5]));
