function solution(priorities, location) {
  var answer = 0;
  let newPriorities = [];
  priorities.forEach((v, i) => {
    newPriorities.push(`${v}-${i}`);
  });
  const value = newPriorities[location];

  while (1) {
    let idx = priorities.indexOf(Math.max(...priorities));
    let temp = newPriorities[idx];

    priorities = [...priorities.slice(idx + 1), ...priorities.slice(0, idx)];
    newPriorities = [
      ...newPriorities.slice(idx + 1),
      ...newPriorities.slice(0, idx),
    ];
    answer++;
    if (value === temp) break;
  }
  return answer;
}

console.log(solution([1, 1, 9, 1, 1, 1], 0)); // 5
