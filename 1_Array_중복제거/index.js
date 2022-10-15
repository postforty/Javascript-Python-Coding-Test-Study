const nums = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8];

// 1. Set()
// const uniqueNums = [...new Set(nums)];
// console.log(uniqueNums);

// 2. indexOf()
// const uniqueNums = nums.filter(
//   (item, position) => nums.indexOf(item) === position
// );
// console.log(uniqueNums);

// 3. caching/frequency map
// loop를 통해 미리 지정된 caching object에 존재 여부 확인
// function uniqueNums(arr) {
//   const uniqueElements = {};
//   const result = [];
//   for (let element of arr) {
//     if (!uniqueElements[element]) {
//       result.push(element);
//     }
//     uniqueElements[element] = element;
//   }
//   return result;
// }
// console.log(uniqueNums(nums));

// 4. object
function uniqueNums(arr) {
  const result = {};
  for (let element of arr) {
    result[element] = element;
  }
  return Object.values(result);
}
console.log(uniqueNums(nums));
