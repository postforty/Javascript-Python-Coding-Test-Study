function solution(s) {
  let answer = 0;
  let newS = s;

  const func = (char) => {
    if (")}]".includes(char[0])) {
      return 0;
    }

    let a = (b = c = 0);
    let prev = "";
    for (let [i, v] of [...char].entries()) {
      if (prev === "[" && ")}".includes(v)) {
        answer = 0;
        return false;
      }
      if (prev === "{" && ")]".includes(v)) {
        answer = 0;
        return false;
      }
      if (prev === "(" && "}]".includes(v)) {
        return 0;
        return false;
      }

      if (v == "[") {
        a += 1;
        prev = v;
        continue;
      }
      if (v == "{") {
        b += 1;
        prev = v;
        continue;
      }
      if (v == "(") {
        c += 1;
        prev = v;
        continue;
      }

      if (v == "]" && a > 0) {
        a -= 1;
      }
      if (v == "}" && b > 0) {
        b -= 1;
      }
      if (v == ")" && c > 0) {
        c -= 1;
      }
      prev = v;
    }

    return a + b + c == 0 ? 1 : 0;
  };

  [...s].forEach((_) => {
    answer += func(newS);
    newS = newS.slice(1, s.length) + newS.slice(0, 1);
  });
  return answer;
}

console.log(solution("[](){}")); // 3
console.log(solution("}[](){")); // 3
console.log(solution("{(})")); // 0
console.log(solution("}}}")); // 0
