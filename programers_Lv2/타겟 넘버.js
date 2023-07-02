function solution(numbers, target) {
  var answer = 0;
  const sumNumbers = numbers.reduce((a, b) => a + b);

  function getSubArr(arr) {
    const subArr = [];

    function backTrack(start, curr) {
      subArr.push([...curr]);

      for (let i = start; i < arr.length; i++) {
        curr.push(arr[i]);
        backTrack(i + 1, curr);
        curr.pop();
      }
    }

    backTrack(0, []);
    return subArr;
  }

  const tempArr = getSubArr(numbers);

  tempArr.forEach((v, i) => {
    if (v.length !== 0) {
      const sumArr = v.reduce((a, b) => a + b);
      answer += sumNumbers - sumArr * 2 === target ? 1 : 0;
    }
  });

  return answer;
}

console.log(solution([1, 1, 1, 1, 1], 3)); // 5
console.log(solution([4, 1, 2, 1], 4)); // 2
