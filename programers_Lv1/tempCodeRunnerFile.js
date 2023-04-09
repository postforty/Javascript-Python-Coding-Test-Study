function solution(n, lost, reserve) {
  var answer = n - lost.length;

  const sortedLost = lost.sort((a, b) => a - b);
  const sortedReserve = reserve.sort((a, b) => a - b);

  const sortedLostRemove = [...sortedLost];

  sortedLost.forEach((value, idx) => {
    if (sortedReserve.indexOf(value) > -1) {
      sortedReserve.splice(sortedReserve.indexOf(value), 1);
      sortedLostRemove.splice(idx, 1);
      answer++;
    }
  });

  const sortedReserveRemove = [...sortedReserve];

  for (let i = 0; i < sortedLostRemove.length; i++) {
    if (sortedReserveRemove.indexOf(sortedLostRemove[i] - 1) > -1) {
      sortedReserveRemove.splice(
        sortedReserveRemove.indexOf(sortedLostRemove[i] - 1),
        1
      );
      answer++;
      continue;
    }
    if (sortedReserveRemove.indexOf(sortedLostRemove[i] + 1) > -1) {
      sortedReserveRemove.splice(
        sortedReserveRemove.indexOf(sortedLostRemove[i] + 1),
        1
      );
      answer++;
    }
  }

  return answer;
}