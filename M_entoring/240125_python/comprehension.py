"comprehension"
# list, dict를 쉽게 만들어줌

numbers = range(1, 10)

square_numbers = []
for number in numbers:
    if number % 2 != 0:
        square_numbers.append(number ** 2)

square_numbers2 = [number ** 2 for number in numbers if number % 2 != 0]


# print(square_numbers)
# print(square_numbers2)


score = [
    {"name": '최지현', "score": 90},
    {"name": '김떙땡', "score": 100},
    {"name": '홍길동', "score": 50}
]

name_with_score = {
    s["name"]: s["score"]
    for s in score
    if s["score"] > 50
}

print(name_with_score)






# 리스트 컴프리헨션

numbers = range(1, 10)

square_numbers = []
for number in numbers:
    square_numbers.append(number ** 2)

square_numbers2 = [number ** 2 for number in numbers if number % 2 != 0]

score = [
    {"name": '최지현', "score": 90},
    {"name": '김떙땡', "score": 100},
    {"name": '홍길동', "score": 50}
]

name_with_score = {
    s["name"]: s["score"]
    for s in score
    if s["score"] > 50
}
