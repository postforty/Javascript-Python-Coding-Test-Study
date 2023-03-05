function solution(s) {
  var answer = [];

  const arr = [...s];
  const temp = {}; // 객체의 키가 중복이 없음을 이용하였음
  temp[arr[0]] = 0;
  arr.shift();
  answer.push(-1);

  for (const i of arr) {
    if (Object.keys(temp).includes(i)) {
      temp[i] += 1;
      answer.push(temp[i]);
      for (const j of Object.keys(temp)) {
        temp[j] += 1;
      }
      temp[i] = 0;
    } else {
      for (const j of Object.keys(temp)) {
        temp[j] += 1;
      }
      temp[i] = 0;
      answer.push(-1);
    }
  }

  return answer;
}

console.log(solution("ssssss"));
