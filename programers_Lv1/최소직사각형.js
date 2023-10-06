function solution(sizes) {
  const [num1, num2] = sizes.reduce(
    (acc, curr) => {
      let [a, b] = acc;
      const [x, y] = curr.sort((a, b) => a - b);
      acc = [x > a ? x : a, y > b ? y : b];
      return acc;
    },
    [0, 0]
  );
  return num1 * num2;
}

console.log(
  solution([
    [60, 50],
    [30, 70],
    [60, 30],
    [80, 40],
  ])
);
