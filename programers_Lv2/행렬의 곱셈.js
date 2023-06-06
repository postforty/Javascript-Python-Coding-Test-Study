function solution(arr1, arr2) {
  var answer = [];

  // newArr2 = [];
  // arr2[0].forEach((_, i) => {
  //   const temp = [];
  //   arr2.forEach((v, j) => {
  //     temp.push(v[i]);
  //   });
  //   newArr2.push(temp);
  // });

  newArr2 = arr2[0].reduce((acc, _, idx) => {
    let rst = [];
    arr2.forEach((v) => {
      rst.push(v[idx]);
    });
    acc = [...acc, rst];
    return acc;
  }, []);

  const func = (arr1, arr2) => {
    let rst = 0;
    arr1.forEach((_, i) => {
      rst += arr1[i] * arr2[i];
    });
    return rst;
  };

  arr1.forEach((v) => {
    const rst = [];
    newArr2.forEach((w) => rst.push(func(v, w)));
    answer.push(rst);
  });

  return answer;
}

console.log(
  solution(
    [
      [1, 4],
      [3, 2],
      [4, 1],
    ],
    [
      [3, 3],
      [3, 3],
    ]
  )
); // [[15, 15], [15, 15], [15, 15]]
