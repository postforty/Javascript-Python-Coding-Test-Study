function solution(keymap, targets) {
  function func(k, t) {
    // const result = [];
    [...t].forEach((v, i) => console.log(v, i));
  }

  func("ABACD", "ABCD");
}

solution();

// console.log(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"])); // [9, 4]
// console.log(solution(["AA"], ["B"])); // [-1]
// console.log(solution(["BC"], ["AC", "BC"])); // [-1,3]
