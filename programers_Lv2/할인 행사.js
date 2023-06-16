function solution(want, number, discount) {
  var answer = 0;
  let num = discount.length - 9;
  for (let i = 0; i < num; i++) {
    const tempArr = discount.slice(i, i + 10);
    const resultCount = want.reduce((acc, cur, idx) => {
      const count = tempArr.filter((i) => i === cur).length;
      acc += count === number[idx] ? 1 : 0;
      return acc;
    }, 0);
    answer += resultCount === want.length && 1;
  }
  return answer;
}

console.log(
  solution(
    ["banana", "apple", "rice", "pork", "pot"],
    [3, 2, 2, 2, 1],
    [
      "chicken",
      "apple",
      "apple",
      "banana",
      "rice",
      "apple",
      "pork",
      "banana",
      "pork",
      "rice",
      "pot",
      "banana",
      "apple",
      "banana",
    ]
  )
); // 3
