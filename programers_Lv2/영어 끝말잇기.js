function solution(n, words) {
  var answer = [];
  const arr1 = [...words];
  const arr2 = [...words.slice(1, words.length)];

  const playersArr = [
    ...arr1.map((item, idx) => ((idx + 1) % n !== 0 ? (idx + 1) % n : n)),
  ];

  const roundArr = [];
  round = 1;
  for (let i = 1; i <= words.length; i++) {
    if (i % n === 0) {
      roundArr.push(round);
      round++;
    } else {
      roundArr.push(round);
    }
  }

  for (let i = 0; i < arr1.length; i++) {
    let w1 = arr1[i];
    let w2 = arr2[i];
    try {
      if (w1.slice(-1) !== w2.slice(0, 1)) {
        answer.push(playersArr[i + 1]);
        answer.push(roundArr[i + 1]);
        break;
      }
      if (arr1.slice(0, i).filter((el) => el == w2).length > 0) {
        answer.push(playersArr[i + 1]);
        answer.push(roundArr[i + 1]);
        break;
      }
    } catch {
      answer = [0, 0];
    }
  }

  return answer;
}

//   console.log(solution(3, ["aa", "ab", "bc", "ca", "aaa", "abb", "bc", "ca", "aa"])) // [1, 3] / 17, 19에서 에러 발생. 해결하기 위해 만든 예제. 리스트 내에 여러개의 중복 요소를 추가하였음
// console.log(
//   solution(3, [
//     "tank",
//     "kick",
//     "know",
//     "wheel",
//     "land",
//     "dream",
//     "mother",
//     "robot",
//     "tank",
//   ])
// ); // [3, 3]
// console.log(
//   solution(5, [
//     "hello",
//     "observe",
//     "effect",
//     "take",
//     "either",
//     "recognize",
//     "encourage",
//     "ensure",
//     "establish",
//     "hang",
//     "gather",
//     "refer",
//     "reference",
//     "estimate",
//     "executive",
//   ])
// ); // [0, 0]
console.log(
  solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])
); // [1, 3]
