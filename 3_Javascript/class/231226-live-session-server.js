// js로도 웹서버를 만들 수 있다.
// 파이썬으로 'Django'라는 프레임워크를 사용해서 웹 서버를 만드는 것처럼 js에서는 다양한 프레임워크를 사용해서 웹서버르 만들 수 있다.

// 파이썬처럼 Js에서도 프레임워크나 라이브러리 없이 웹서버를 만들 수 있다.(내장 라이브러리만 사용)

// server = req를 response 주는 거

const http = require("http");
const host = "localhost";
const port = 5555;
const server = http.createServer();
