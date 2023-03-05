function solution(polynomial) {
  var temp = polynomial.split(" + ");
  var x = 0;
  var n = 0;
  for (var i of temp) {
    if (i.length === 1 && i === "x") {
      x += 1;
    } else if (i.length === 2 && i.includes("x")) {
      x += parseInt(i.slice(0, 1));
    } else if (i.length === 3 && i.includes("x")) {
      x += parseInt(i.slice(0, 2));
    } else {
      n += parseInt(i);
    }
  }
  var xStr = x > 1 ? x + "x" : x == 1 ? "x" : 0;
  var nStr = n !== 0 ? n : 0;
  if (xStr !== 0 && nStr !== 0) {
    answer = xStr + " + " + nStr;
  } else if (xStr !== 0 && nStr === 0) {
    answer = xStr.toString();
  } else {
    answer = nStr.toString();
  }

  return answer;
}

console.log(solution("15 + 99 + x"));
