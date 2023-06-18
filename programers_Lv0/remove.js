const arr = [1, 2, 3, 4, 5];

const rm = 3;

const remove = (arr, rm) => {
  let idx = arr.indexOf(rm);
  arr.splice(idx, 1);
  return arr;
};

console.log(remove(arr, rm));
