# 반복 대상을 설정할 수 있음 리스트, 튜플, 딕셔너리 등 순회할 수 있는 구조는 for을 활용할 수 있음
my_list = [1, 2, 3]

for x in my_list:
    print(x)  # 리스트의 원소값이 담겨져 있음

my_tuple = (1, 2, 3)

for x in my_tuple:
    print(x)  # 튜플의 원소값이 담겨져 있음

person = {"이름": "gogleset", "나이": 8}


# 값 출력
for v in person.values():
    print(v)
# 키 출력
for k in person.keys():
    print(k)
# 다 출력
for k, v in person.items():
    print(k, v)

# 문자도 가능
my_fruit = "apple"
for x in my_fruit:
    print(x)
