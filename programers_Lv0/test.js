const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input = [line];
}).on("close", function () {
  str = input[0];
    arr = [...str];
    console.log(
      arr
        .map((el) => {
          if (el === el.toUpperCase) {
            return el.toLowerCase;
          } else {
            return el.toUpperCase;
          }
        })
        .join("")
    );
});
