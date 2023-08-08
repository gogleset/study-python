# 클래스는 변수와 함수가 같이 있는 설계서이다.

name = "까망이"
resolution = "FHD"
price = 200000
color = "black"


# class 클래스명: (이름은 카멜케이스 맨 처음엔 대문자)
class BlackBox:
    name


# 인스턴스 추가
b1 = BlackBox()
b1.name = "까망이"
print(b1.name)
print(isinstance(b1, BlackBox))  # b1의 인스턴스가 맞는지 확인

# b2 = BlackBox()
# print(b2.name)  # error


class BlackBox2:
    # 생성자 함수 만들기, 객체가 생성될때 자동으로 실행해줌
    def __init__(self, price, name):
        self.price = price
        self.name = name


# 생성자 함수로 인스턴스만들기
b3 = BlackBox2(2000, "까망이")
print(b3.name)
