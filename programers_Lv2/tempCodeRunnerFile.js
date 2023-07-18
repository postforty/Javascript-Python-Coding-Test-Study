function solution(X, Y) {
  let xArr = [...X];
  let yArr = [...Y];
  const xObj = xArr.reduce((acc, curr) => {
    acc[curr] === undefined ? (acc[curr] = 1) : (acc[curr] += 1);
    return acc;
  }, {});
  const yObj = yArr.reduce((acc, curr) => {
    acc[curr] === undefined ? (acc[curr] = 1) : (acc[curr] += 1);
    return acc;
  }, {});

  const set1 = new Set(xArr);
  const intersection = yArr.filter((v) => set1.has(v));

  if (intersection.length === 0) return "-1";

  let answer = "";
  answer = intersection.sort((a, b) => b - a).join("");

  return answer.slice(0, 1) === "0" ? "0" : answer;
}
