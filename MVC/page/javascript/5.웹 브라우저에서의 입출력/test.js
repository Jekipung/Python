///대화상자

//1. 경고 대화상자
alert('경고합니다!');

//2. 입력 대화상자
let myname = prompt('이름을 입력하세요');
alert('이름:' + myname);

//3. 확인 대화상자
let check = confirm('링크를 표시하시겠습니까?');
if (check) {
    alert("확인을 눌렀습니다.");
} else {
    alert("취소를 눌렀습니다.");
}

///cossole

console.dir({test : '테스트 객체입니다.'});
console.log('일반 로그입니다.');
console.info('메시지타입 로그입니다.');
console.warn('경고 로그입니다.');
console.error('에러 로그입니다.');