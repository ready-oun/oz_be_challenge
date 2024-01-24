// https://drive.google.com/file/d/1xIFZrztqY-b1qpC0mvqZSIAvmSB4nYuv/view?usp=sharing

// 요소 선택 및 배열 선언
const todoList = document.getElementById("todo-list");
const todoForm = document.getElementById("todo-form");
let todoArr = [];

// 로컬 저장소에 저장하기
function saveTodos() {
  const todoString = JSON.stringify(todoArr);
  localStorage.setItem("myTodos", todoString);
}

// 로컬 저장소에서 가져오기
function loadTodos() {
  const myTodos = localStorage.getItem("myTodos");
  if (myTodos !== null) {
    todoArr = JSON.parse(myTodos);
    displayTodos();
  }
}

loadTodos();

// 할일 삭제하기
function handleTodoDelBtnClick(clickedId) {
  // clickedId를 제외하고 나머지만 남기는 Filter
  todoArr = todoArr.filter(function (aTodo) {
    return aTodo.todoId !== clickedId;
  });
  displayTodos();
  saveTodos();
}

// 할일 수정하기
function handleTodoItemClick(clickedId) {
  todoArr = todoArr.map(function (aTodo) {
    if (aTodo.todoId === clickedId) {
      // 내가 클릭한 투두에 해당하는 아이디가 맵에서 나왔다
      return {
        ...aTodo, // 그럼 기존의 투두 내용에다가 투두던을 반전시켜서 추가한다.
        todoDone: !aTodo.todoDone, // 기존 aTodo 내용을 todoDone에 false(반대) 상태로 덮어써서 리턴한다.
      };
    } else {
      return aTodo;
    }
  });
  // 확인차 console.log(todoArr); 여기서 aTodo를 클릭했을 때, TodoDone이 True가 콘솔에 뜨는지 확인
  displayTodos();
  saveTodos();
}

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
  displayTodos(); // added it to update the display
  saveTodos(); //로컬 스토리지에 추가하는 함수 호출
});

// displayTodos 함수:할일이 하나씩 추가될 때마다 보여주는 함수
function displayTodos() {
  todoArr = todoArr || []; // added to chked if todoArr is null or undefined, and initialize it as an empty array
  todoList.innerHTML = ""; // 기존 내용을 지우면서 시작한다 = 기존에 추가한 Input이 display 중임에도 새로운 input이 추가될 때마다 같이 중복되어 또 추가되므로, 기존 내용을 빈칸으로 만들어주는 작업.
  todoArr.forEach(function (aTodo) {
    // 배열의 요소 수 == 내 할일 목록 개수
    const todoItem = document.createElement("li"); // 리스트는 ul에 들어갈 거고, ul은 li를 쓰므로 ul이 아닌 li를 작성.
    const todoTextContainer = document.createElement("div"); // added container for the complete todo text

    const todoDelBtn = document.createElement("span"); // 삭제 버튼을 넣기 위한 텍스트 영역을 생성해서
    todoDelBtn.textContent = "x"; // 삭제를 의미하는 x 추가

    todoTextContainer.textContent = aTodo.todoText; // added to display the complete todo text
    todoItem.appendChild(todoTextContainer); // added
    // todoItem.textContent = aTodo.todoText; // 개체.속성명 / toBeAdded = {todoText: todoForm.todo.value ...}
    if (aTodo.todoDone) {
      todoItem.classList.add("done");
    } else {
      todoItem.classList.add("yet");
    }
    todoItem.title = "it will be done if you'd click it";
    todoDelBtn.title = "it will be deleted if you'd click it";

    todoItem.addEventListener("click", function () {
      handleTodoItemClick(aTodo.todoId);
    });

    todoDelBtn.addEventListener("click", function () {
      handleTodoDelBtnClick(aTodo.todoId);
    });
    todoItem.appendChild(todoDelBtn);
    todoList.appendChild(todoItem);
  });
}
