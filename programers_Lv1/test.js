const sum = (...values) => {
  let sum = 0;
  for (const value of values) {
    sum += value;
  }
  return sum;
};

console.log(sum(1, 2, 1, 1, 1, 1)); // 7
console.log(sum(1, 1)); // 2
