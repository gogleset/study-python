# 함수 안에 있는 변수는 함수 안에서만 호출 할 수 있다


def secret():
    # 지역변수 message
    message = "이건 나만의 비밀"


def secret1():
    # 지역변수 message
    message = "이건 나만의 비밀1"


print(secret())
