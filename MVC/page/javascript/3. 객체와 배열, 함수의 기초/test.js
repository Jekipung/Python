///객체

//객체 리터럴로 객체 생성
//프로퍼티로 suit, rank를 가지는 객체
let card = {suit : '하트', rank : 'A'};
console.log(card);

//프로퍼티의 이름은 문자열이 되어도 상관없다.
card = {'suit' : '하트', 'rank' : 'A'};
console.log(card.suit);
console.log(card["rank"]);
console.log(card.test);

//프로퍼티의 값 추가
card.value = 14;
console.log(card.value)

//객체의 프로퍼티 삭제
delete card.value;
console.log(card.value);

//객체의 프로퍼티 보유 여부 확인
console.log("suit" in card);
console.log("random" in card);

console.log("toString" in card);

///메서드
card = {
    suit : "하트",
    rank : "A",
    showCard: function(){
        //this 키워드는 함수의 소유자를 가르킨다.
        console.log(`이 카드는 ${this.suit} ${this.rank} 입니다.`)
    }
};
card.showCard();

///함수
function square(x){
    return x * x;
}
console.log(square(9))

//함수는 객체다.
//객체와 동일한 조작이 가능하다/
square.test = "testValue"
console.log(square.test)

///객체 생성자
function Card(suit, rank){
    console.log('소유자' + this)
    //new 키워드가 붙은 경우
    //this = {};
    this.suit = suit;
    this.rank = rank;
    //nes 키워드가 붙은 경우
    //return this;
}

card = new Card("하트", "A");
console.log(card);

//전역 함수의 this는 기본적으로
//글로벌 객체인 window를 가리킨다.
card = Card("하트", "A")
console.log(window.suit, window.rank);

///클래스 (ES6버전 생성자)
function Circle(center, radius){
    this.censter = center;
    this.radius = radius;
    this.area = function(){
        return Math.PI * this. radius * this.radius;
    }
}

let circle = new Circle({x: 0, y: 0}, 2.0);
console.log(`넓이 = ${circle.area()}`);

function Product(name,weight){
    this.name = name;
    this.weight = weight;
    this.price = function(){
        return weight * 16.9;
    }
}

let price = new Product("삼겹살", 150);
console.log(`가격 = ${price.price()}`)

