function solution(common) {
  var answer = 0;
  if (common[1] / common[0] === common[2] / common[1]) {
    answer = (common[1] / common[0]) * common.pop();
  }
  if (common[1] - common[0] === common[2] - common[1]) {
    answer = common[1] - common[0] + common.pop();
  }
  return answer;
}
console.log(solution([1, 2, 3, 4]));
