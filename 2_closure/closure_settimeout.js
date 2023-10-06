// 1초 후 10 출력
var i;
for (i = 0; i < 10; i++) {
  setTimeout(() => console.log(i), 1000);
}

// 1초 후 0~9까지 출력
var i;
for (i = 0; i < 10; i++) {
  ((j) => setTimeout(() => console.log(j), 1000))(i);
}

// 1초 후 0~9까지 출력
// let 키워드 사용시 즉시 실행함수를 적용하지 않아도 0~9 출력하고 있음
for (let i = 0; i < 10; i++) {
  setTimeout(function () {
    console.log(i);
  }, 1000);
}

// 1초 후 0~9까지 출력
var i;
for (i = 0; i < 10; i++) {
  (function (j) {
    setTimeout(function () {
      console.log(j);
    }, 1000);
  })(i);
}
