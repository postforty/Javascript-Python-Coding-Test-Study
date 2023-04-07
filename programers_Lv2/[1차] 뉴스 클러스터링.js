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

  if (str1Arr.length === 0) {
    return 0;
  }

  str1Arr.sort();
  str2Arr.sort();

  if (JSON.stringify(str1Arr) === JSON.stringify(str2Arr)) return 65536;

  // 합집합
  unionTemp = [...str1Arr];
  unionResult = [...str1Arr];

  for (let i of str2Arr) {
    if (!unionTemp.includes(i)) {
      unionResult.push(i);
    } else {
      for (let j = 0; j < unionTemp.length; j++) {
        if (unionTemp[j] === i) {
          unionTemp.splice(j, 1);
          break;
        }
      }
    }
  }

  let unionCnt = unionResult.length;

  // 교집합
  const intersectionResult = [];

  const tempArr = [...str1Arr];

  for (let i = 0; i < str2Arr.length; i++) {
    if (tempArr.indexOf(str2Arr[i]) !== -1) {
      intersectionResult.push(tempArr[tempArr.indexOf(str2Arr[i])]);
      tempArr.splice(tempArr.indexOf(str2Arr[i]), 1);
    }
  }

  console.log(intersectionResult);

  let intersectionCnt = intersectionResult.length;

  answer = Math.floor((intersectionCnt / unionCnt) * 65536);
  return answer;
}

console.log(solution("FRANCE", "french")); // 16384
console.log(solution("aa1+aa2", "AAAA12")); // 43690
console.log(solution("E=M*C^2", "e=m*c^2")); // 65536
console.log(solution("handshake", "shake hands")); // 65536
console.log(solution("", "")); // 65536
console.log(solution("1111", "bcdefg")); // 65536
