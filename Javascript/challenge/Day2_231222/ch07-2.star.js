// 첫 줄에 별을 하나 찍고 다음 줄로 넘어갈 수록 개수가 하나씩 늘게 반복

// 첫 번째 별 모양 생성
let parentEle = document.getElementById("star1_p"); // 'star1' 아이디를 가진 부모 엘리먼트를 찾음
// let star1 = document.createElement("div"); // 새로운 div 엘리먼트를 생성하여 star1 변수에 할당

for (let i = 0; i < 5; i++) {
  let line = document.createElement("p"); // 새로운 p 엘리먼트를 생성하여 각 줄을 표현할 변수 line에 할당
  for (let j = 0; j <= i; j++) {
    line.textContent += "*"; // 줄에 '*' 문자열을 추가하여 별을 그림
  }
  star1.appendChild(line); // 각 줄을 star1에 추가
}

parentEle.appendChild(star1); // 부모 엘리먼트에 star1을 추가하여 별을 표시

// 두 번째 별 모양 생성
let parentEle2 = document.getElementById("star2"); // 'star2' 아이디를 가진 부모 엘리먼트를 찾음
let star2 = document.createElement("div"); // 새로운 div 엘리먼트를 생성하여 star2 변수에 할당

for (let i = 0; i < 5; i++) {
  let line = document.createElement("p"); // 새로운 p 엘리먼트를 생성하여 각 줄을 표현할 변수 line에 할당
  for (let j = 0; j <= i; j++) {
    line.textContent += "*"; // 줄에 '*' 문자열을 추가하여 별을 그림
  }
  star2.appendChild(line); // 각 줄을 star2에 추가
}

for (let i = 5; i > 0; i--) {
  let line = document.createElement("p"); // 역삼각형을 그리기 위해 다시 p 엘리먼트를 생성하여 각 줄을 표현할 변수 line에 할당
  for (let j = 0; j <= i; j++) {
    line.textContent += "*"; // 줄에 '*' 문자열을 추가하여 역삼각형을 그림
  }
  star2.appendChild(line); // 각 줄을 star2에 추가
}

parentEle2.appendChild(star2); // 부모 엘리먼트에 star2를 추가하여 두 번째 별 모양을 표시

// 세 번째 별 모양 생성
let parentEle3 = document.getElementById("star3"); // 'star3' 아이디를 가진 부모 엘리먼트를 찾음
let star3 = document.createElement("div"); // 새로운 div 엘리먼트를 생성하여 star3 변수에 할당

const half = parseInt(10 / 2); // 별 모양의 중간 위치를 계산

// 위쪽 삼각형을 그리기
for (let i = 1; i <= half; i++) {
  let line = document.createElement("p"); // 새로운 p 엘리먼트를 생성하여 각 줄을 표현할 변수 line에 할당
  for (let j = 0; j < half - i; j++) {
    line.textContent += "\u00A0"; // 공백 문자를 추가하여 공백을 표현
  }
  for (let j = 0; j < 2 * i - 1; j++) {
    line.textContent += "*"; // 줄에 '*' 문자열을 추가하여 삼각형을 그림
  }
  star3.appendChild(line);
}

// 아래쪽 역삼각형을 그리기
for (let i = 4; i > 0; i--) {
  let line = document.createElement("p"); // 역삼각형을 그리기 위해 다시 p 엘리먼트를 생성하여 각 줄을 표현할 변수 line에 할당
  for (let j = 0; j < 5 - i; j++) {
    line.textContent += "\u00A0"; // 공백 문자를 추가하여 공백을 표현
  }
  for (let j = 0; j < 2 * i - 1; j++) {
    line.textContent += "*"; // 줄에 '*' 문자열을 추가하여 역삼각형을 그림
  }
  star3.appendChild(line);
}

parentEle3.appendChild(star3); // 부모 엘리먼트에 star3을 추가하여 세 번째 별 모양을 표시
