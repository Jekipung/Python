//  Latin-1 또는 ASCII
let bye = "Good \x62\x79\x65";
console.log(bye);

// 4자리 유니코드
let hello = "반\uAC00워요!";
console.log(hello);

// 16진수 코드 포인트
let readBook = 'Read my javascript \u{1F4D6}';
console.log(readBook)


// 논리 값

let x = 3;

let good = (x == 3);
let bad = (x == 2);

console.log(good);
console.log(bad);

// 특수 한 값 null,  undefined
let empty;
console.log(empty); // 의도하지 않은 결과 undefined

empty = null;
console.log(empty); // 의도한 결과 null

// 심볼: 자기 자신을 제외한 그 어떤 값과도 다른 값

// 심볼 생성
let sym1 = Symbol();
let sym2 = Symbol();

// Symbol()은 호출할 때마다 새로운 값을 만듬
console.log(sym1 == sym2);

// Symbol()에 인수를 전달하면 설명을 덧붙일 수 있음
let HEART = Symbol("하트");
console.log(HEART.toString());

// Symbol.for 메서드를 활용하면 문자열을 키값으로 동일한 심볼을 생성할 수 있다.
let sym3 = Symbol.for("club");
let sym4 = Symbol.for("club");
console.log(sym3==sym4);

// 덧붙이는 설명과는 다르다.
let sym5 = Symbol("club");
console.log(sym4 == sym5);

let name = "Park";
let string = 'Hello ${name}';
console.log(string);    

// 탬플릿 리터럴

console.log(`
안녕하세요
반갑습니다.
`);

let a = 5;
let b = 10;
console.log(a + '+' + b + '=' + (a + b));

console.log(`${a} + ${b} = ${a+b}`)