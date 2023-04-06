function solution(str1, str2) {
  var answer = 0;

  const a2z = new Array(26)
    .fill()
    .map((_, i) => String.fromCharCode(i + 97))
    .join("");

  const createArr = (str) => {
    const strArr = [];
    let i = 0;
    while (i < str.length - 1) {
      const temp = str.substr(i, 2).toLowerCase();
      let count = 0;
      for (t of temp) {
        if (a2z.indexOf(t) !== -1) {
          count++;
        }
      }
      count === 2 && strArr.push(temp);
      count = 0;
      i++;
    }
    return strArr;
  };

  const str1Arr = createArr(str1);
  const str2Arr = createArr(str2);

  if (str2Arr.length === 0) {
    return 65536;
  }

  str1Arr.sort();
  str2Arr.sort();
  if (JSON.stringify(str1Arr) == JSON.stringify(str2Arr)) return 65536;

  const totalArr = [...str1Arr, ...str2Arr];

  const intersectionResultArr = str1Arr.filter((el) => str2Arr.includes(el));

  intersectionResultArr.forEach((el) => {
    for (let i = 0; i < totalArr.length; i++) {
      if (totalArr[i] === el) {
        totalArr.splice(i, 1);
        i--;
        break;
      }
    }
  });

  let intersectionCount = intersectionResultArr.length;
  let unionCount = totalArr.length;

  answer = Math.floor((intersectionCount / unionCount) * 65536);
  return answer;
}

// console.log(solution("FRANCE", "french")); // 16384
// console.log(solution("aa1+aa2", "AAAA12")); // 43690
// console.log(solution("E=M*C^2", "e=m*c^2")); // 65536
// console.log(solution("handshake", "shake hands")); // 65536
// console.log(solution("", "")); // 65536
console.log(solution("1111", "bcdefg")); // 65536
