function solution(k, dungeons) {
  var answer = 0;

  function permutation(arr) {
    if (arr.length === 0) {
      return [[]];
    }
    const result = [];
    for (let i = 0; i < arr.length; i++) {
      const current = arr[i];
      const remaining = [...arr.slice(0, i), ...arr.slice(i + 1)];
      const subPermutations = permutation(remaining);
      for (let j = 0; j < subPermutations.length; j++) {
        const permutation = [current, ...subPermutations[j]];
        result.push(permutation);
      }
    }
    return result;
  }

  const nPr = permutation(dungeons);
  nPr.forEach((v) => {
    let curK = k;
    let cnt = 0;
    v.forEach((w) => {
      if (curK >= w[0]) {
        curK -= w[1];
        cnt++;
      }
    });
    if (cnt > answer) {
      answer = cnt;
    }
  });

  return answer;
}

console.log(
  solution(80, [
    [80, 20],
    [50, 40],
    [30, 10],
  ])
); // 3
