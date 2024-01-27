# lambda

def a(x, y):
    return x - y

# print(a(1,2))
#
# print((lambda x, y: x - y)(1, 2))


score = [
    {"name": '최지현', "score": 90},
    {"name": '김떙땡', "score": 100},
    {"name": '홍길동', "score": 50}
]

sorted(score, key=lambda x: x["score"], reverse=True)
