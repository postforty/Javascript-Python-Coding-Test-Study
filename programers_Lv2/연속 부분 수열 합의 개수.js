function solution(elements) {
  var answer = new Set(elements);

  for (let i = 2; i <= elements.length; i++) {
    elements.forEach((_) => {
      const sum = elements.slice(0, i).reduce((acc, cur) => acc + cur, 0);
      answer.add(sum);
      elements = [...elements.slice(1), ...elements.slice(0, 1)];
    });
  }
  return answer.size;
}
console.log(solution([7, 9, 1, 1, 4])); // 18
