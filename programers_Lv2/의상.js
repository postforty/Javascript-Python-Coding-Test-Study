function solution(clothes) {
  const obj = clothes.reduce((acc, curr) => {
    const [_, b] = curr;
    acc[b] = acc[b] ? acc[b] + 1 : 2;
    return acc;
  }, {});
  let answer = Object.values(obj).reduce((acc, curr) => (acc *= curr));
  return answer - 1;
}

console.log(
  solution([
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
  ])
); // 5
