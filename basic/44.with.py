# 자동으로 파일 닫기
f = open("list.txt", "w", encoding="utf-8")

# with 문법을 쓰게 되면 close()를 쓰지 않아도 자동으로 닫게됨 맨 마지막은 받는 변수이름을 as 뒤에 적은다.
with open("list.txt", "w", encoding="utf-8") as f:
    f.write("askd")


f = open("list.txt", "r", encoding="utf-8")

with open("list.txt", "r", encoding="utf-8") as f:
    contents = f.read()
    print(contents)
