function solution(k, tangerine) {
  let map = new Map();

  tangerine.forEach((v) => {
    if (map.has(v)) {
      map.set(v, map.get(v) + 1);
    } else {
      map.set(v, 1);
    }
  });

  const arr = [...map.values()];

  arr.sort((a, b) => a - b);

  let sum = (cnt = 0);
  while (true) {
    sum += arr.pop();
    cnt++;
    if (sum >= k) {
      return cnt;
    }
  }
}

console.log(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])); // 2
