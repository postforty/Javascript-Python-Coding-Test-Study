function solution(n, a, b) {
  var answer = 0;

  let arr = new Array(n);
  arr.fill(0);
  arr[a - 1] = 1;
  arr[b - 1] = 2;

  function func(param) {
    let newArr = [];
    while (param.length > 1) {
      let a = param.pop();
      let b = param.pop();
      // shift 메서드의 경우 시간 초과 발생
      // shift(): shift()는 첫 번째 요소를 제거하고, 배열의 모든 요소를 앞으로 이동시키는 작업을 수행합니다. 이 작업은 배열의 길이에 따라 선형적인 시간복잡도(O(n))를 가지므로, 배열의 크기가 커질수록 성능이 저하될 수 있습니다.
      // pop(): pop()은 마지막 요소를 제거하기 때문에 배열의 길이에 영향을 주지 않습니다. 배열의 길이와 상관없이 상수 시간복잡도(O(1))를 가지므로, shift()에 비해 성능이 더 우수합니다.
      // let a = param.shift();
      // let b = param.shift();
      newArr.push(a + b);
    }
    return newArr;
  }

  while (true) {
    // arr = func([...arr]); // 이 코드도 가능
    arr = func(arr);
    answer++;

    // Math.max()를 이용해 최대 값이 3일 경우 종료하는 코드 테스트시 런타임 에러 발생
    // filter 메서드로 0이 아닌 값이 1개([1, 2]가 아닌 [3])인 경우에 break하여 통과할 수 있었음
    let check = arr.filter((el) => el !== 0);
    if (check.length < 2) {
      break;
    }
  }

  return answer;
}

console.log(solution(8, 4, 7)); // 3
// console.log(solution(8, 3, 7)); // 3
// console.log(solution(8, 2, 7)); // 3
