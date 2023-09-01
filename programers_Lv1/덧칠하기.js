function solution(n, m, section) {
  var answer = 1;
  let end = section[0] + m - 1;

  section.slice(1, section.length).forEach((v) => {
    if (end < v) {
      answer++;
      end = v + m - 1;
    }
  });
  return answer;
}

console.log(solution(8, 4, [2, 3, 6])); // 2
