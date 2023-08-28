function outer() {
  let i = 0;
  function inner(x) {
    i += x;
    return i;
  }
  return inner;
}

const a = outer();
const b = outer();
console.log("a: ", a(1));
console.log("a: ", a(1));
console.log("a: ", a(1));
console.log("a: ", a(1));
console.log("a: ", a(1));
console.log("b: ", b(1));
console.log("b: ", b(1));
console.log("a: ", a(1));
console.log("a: ", a(1));
