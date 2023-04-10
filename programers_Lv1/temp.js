const arr = [1, 2, 3, 4, 5];

const rm = [5, 1];

const remove = (arr, rm) => {
  for (let i = 0; i < rm.length; i++) {
    let idx = arr.indexOf(rm[i]);
    arr.splice(idx, 1);
  }
  return arr;
};

console.log(remove(arr, rm));
