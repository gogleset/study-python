# 전역에서 접근 가능한 변수
number = 1


def get_number():
    print(number)


def get_string():
    # 지역변수
    number = 3
    print(str(number))


def get_value():
    # global 키워드로 전역변수 사용하겠다 없다면 만들어내겠다
    global number
    # 이럼 또 지역변수가됨
    number = 5
    print(str(number))


get_number()
get_string()
get_value()
