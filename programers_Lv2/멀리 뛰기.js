function solution(n) {
  if (n == 1) return n;

  let a = 1;
  let b = 2;

  for (const _ of Array.from({ length: n - 2 }, (_, i) => i)) {
    temp = a;
    a = b;
    b = (temp + b) % 1234567;
  }

  return b;
}

console.log(solution(6)); // 13
