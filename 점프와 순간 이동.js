function solution(n) {
  var ans = 1;
  let divN = n;

  while (divN > 1) {
    if (divN % 2 !== 0) {
      divN = parseInt(divN / 2);
      ans++;
    } else {
      divN = divN / 2;
    }
  }

  return ans;
}

console.log(solution(5)); // 2
console.log(solution(6)); // 2
console.log(solution(5000)); // 5
