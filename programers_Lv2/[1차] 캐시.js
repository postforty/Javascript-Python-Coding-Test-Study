function solution(cacheSize, cities) {
  let answer = 0;
  if (cacheSize === 0) {
    return cities.length * 5;
  }
  const cache = new Array(cacheSize);
  const lowCities = cities.map((v) => v.toLowerCase());
  lowCities.forEach((v, i) => {
    let idx = cache.indexOf(v);
    if (idx > -1) {
      cache.push(...cache.splice(idx, 1));
      answer++;
    } else {
      answer += 5;
      cache.shift();
      cache.push(v);
    }
  });
  return answer;
}

// console.log(
//   solution(3, [
//     "Jeju",
//     "Pangyo",
//     "Seoul",
//     "NewYork",
//     "LA",
//     "Jeju",
//     "Pangyo",
//     "Seoul",
//     "NewYork",
//     "LA",
//   ])
// ); // 50
console.log(
  solution(3, [
    "Jeju",
    "Pangyo",
    "Seoul",
    "Jeju",
    "Pangyo",
    "Seoul",
    "Jeju",
    "Pangyo",
    "Seoul",
  ])
); // 21
