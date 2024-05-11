// JS의 변수 var, let, const
// 한줄 주석
/*
여러줄 주석
*/
var x; // x라는 식별자로 변수 생성
console.log(x); // undefined 출력

x = 5; // 5를 x에 대입
console.log(x); // 5 출력

// 변수를 여러개 입력 및 초기화
var a = 1, b = 2, c = 3;

// 선언되지 않은 변수 참조: 참조 에러
// console.log(y);

// 호이스팅 - 변수 선언 끌어올림
// JS는 실행시 먼저 실행을 위한 환경을 구성하기 때문에, 컨텍스트 내의 변수를 미리 준비함.
console.log(t);
var t = 5;

// let과 const
// console.log(k) let은 var과 달리 호이스팅 X
let k = 10;
k = 9;
console.log(k)

// const는 상수 선언
// 초기화와 동시에 값을 대입, 그 뒤 변경 X
const PI = 3.141592;
PI = 1.414;