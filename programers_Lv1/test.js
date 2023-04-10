function solution(n, lost, reserve) {
  var answer = 0;

  const sortedLost = lost.sort((a, b) => a - b);
  const sortedReserve = reserve.sort((a, b) => a - b);

  const totalObj = [];
  for (let i = 1; i <= n; i++) {
    totalObj.push({ value: i, state: true });
  }

  const lostObj = [];
  sortedLost.forEach((el) => lostObj.push({ value: el, state: true }));

  const reserveObj = [];
  sortedReserve.forEach((el) => reserveObj.push({ value: el, state: true }));

  // 체육복 분실 처리
  for (const lost of lostObj) {
    for (const total of totalObj) {
      if (lost.value === total.value) {
        total.state = false;
      }
    }
  }

  // 체육복 두벌 처리
  for (const lost of lostObj) {
    for (const reserve of reserveObj) {
      if (lost.value === reserve.value) {
        totalObj.filter((el) => lost.value === el.value)[0].state = true;
        lost.state = false;
        reserve.state = false;
      }
    }
  }

  // 체육복 좌 처리
  for (const lost of lostObj) {
    if (lost.state) {
      for (const reserve of reserveObj) {
        if (totalObj.filter((el) => lost.value === el.value).length !== 0) {
          totalObj.filter((el) => lost.value === el.value)[0].state = true;
          lost.state = false;
          reserve.state = false;
        }
      }
    }
  }

  // 체육복 우 처리
  for (const lost of lostObj) {
    if (lost.state) {
      for (const reserve of reserveObj) {
        if (totalObj.filter((el) => lost.value === el.value).length !== 0) {
          totalObj.filter((el) => lost.value === el.value)[0].state = true;
          lost.state = false;
          reserve.state = false;
        }
      }
    }
  }

  answer = totalObj.filter((el) => el.state === true).length;

  return answer;
}

console.log(solution(5, [2, 4], [1, 3, 5]));
console.log(solution(5, [2, 4], [3]));
console.log(solution(3, [3], [1]));
console.log(solution(5, [4, 2], [3, 5]));
console.log(solution(4, [2, 3], [3, 4]));
console.log(solution(4, [3, 2], [3, 4, 2]));
