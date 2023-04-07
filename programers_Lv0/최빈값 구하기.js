function solution(array) {
  var answer = 0;

  const setArr = [...new Set(array)];

  if (setArr.length === 1) {
    return setArr[0];
  }

  const setObj = Object.fromEntries(Array.from(setArr, (a) => [a, 0]));

  array.forEach((el) => setObj[el]++);

  // 객체 내림차순 정렬
  var sortable = [];
  for (var name in setObj) {
    sortable.push([name, setObj[name]]);
  }
  sortable.sort(function (a, b) {
    return b[1] - a[1];
  });

  if (sortable[0][1] === sortable[1][1]) {
    return -1;
  }

  answer = Number(sortable[0][0]);

  return answer;
}

console.log(solution([1, 2, 3, 3, 3, 4]));
