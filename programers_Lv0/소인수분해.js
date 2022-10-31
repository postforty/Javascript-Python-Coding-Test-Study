function solution(n) {
  var answer = [];
  const range = Array.from({ length: n }, (v, i) => i + 1); // 1부터 n까지 숫자를 배열로 만들기
  const newRange = range.splice(1); // 배열에서 불필요한 1을 제외
  let i = 0;
  let num = n;
  while (newRange[newRange.length - 1] !== i) {
    if (num % newRange[i] !== 0) {
      i++;
    }
    if (num % newRange[i] === 0) {
      num = num / newRange[i];
      answer.push(newRange[i]);
    }
  }
  answer = Array.from(new Set(answer)); // 중복값 제거 후 Set타입을 배열로 변경
  return answer;
}
console.log(solution(420));
