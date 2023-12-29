// https://drive.google.com/file/d/1xIFZrztqY-b1qpC0mvqZSIAvmSB4nYuv/view?usp=sharing

// 요소 선택 및 배열 선언
const todoList = document.getElementById("todo-list");
const todoForm = document.getElementById("todo-form");
let todoArr = [];

// 할일 추가, 표시, 수정, 삭제하기 각각 !

// 할일 추가하는 액션 함수
todoForm.addEventListener("submit", function (e) {
  e.preventDefault(); // submit 시 새로고침하지 않도록
  const toBeAdded = {
    todoText: todoForm.todo.value, // get value from name="todo" @html
    todoId: new Date().getTime(), // new DAte() : 추가될 때 그 시간에 대한 정보를 식별값으로 가지게 해서 getTime()으로 숫자형태로 가지게(시간을 정수 형태로)
    todoDone: false, // 모든 할일은 추가될 때마다 다 하지 않은 상태 (Not done)이므로.
  }; // arr 키 밸류 값들 사이 콤마(,)로 나눠주지 않으면 에러가 발생한다.
  todoForm.todo.value = ""; // 작성하고 추가한 할일(input)을 작성칸에서 지우겠다(==빈칸으로 만들겠다).
  todoArr.push(toBeAdded); // ()가 아니라 {}를 작성해서 에러 발생함.
});

// displayTodos 함수:할일이 하나씩 추가될 때마다 보여주는 함수
function displayTodos() {
  todoList.innerHTML = ""; // 기존 내용을 지우면서 시작한다 = 기존에 추가한 Input이 display 중임에도 새로운 input이 추가될 때마다 같이 중복되어 또 추가되므로, 기존 내용을 빈칸으로 만들어주는 작업.
  todoArr.forEach(function (aTodo) {
    // 배열의 요소 수 == 내 할일 목록 개수
    const todoItem = document.createElement("li"); // 리스트는 ul에 들어갈 거고, ul은 li를 쓰므로 ul이 아닌 li를 작성.
    const todoDelBtn = document.createElement("span"); // 삭제 버튼을 넣기 위한 텍스트 영역을 생성해서
    todoDelBtn.textContent = "x"; // 삭제를 의미하는 x 추가
    todoItem.textContent = aTodo.todoText; // 개체.속성명 / toBeAdded = {todoText: todoForm.todo.value ...}
    todoItem.title = "클릭하면 완료됨";
    todoDelBtn.title = "클릭하면 삭제됨";

    todoDelBtn.appendChild(todoDelBtn);
    todoList.appendChild(todoItem);
  });
}

// handleTodoDelBtnClick 함수

// handleTodoItemClick 함수

// saveTodos 함수

// loadTodos 함수

// 할일 입력 후 제출하면 발생하는 이벤트 핸들링

// 시작할 때 한번만!