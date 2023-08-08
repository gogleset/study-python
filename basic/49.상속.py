class BlackBox:
    def __init__(self, price, name):
        self.price = price
        self.name = name


class TravelBlackBox:
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def set_travel_mode(self, min):
        print(f"{min}분동안 여행모드 ON")


# BlackBox와 TravelBlackBox는 닮은 점이 있다. init 함수가 같다는 점이다


# 상속을 이용해보자, 자식 클래스로 만들어진다.
# 문법은 class class명(부모 클래스)
class TravelBlackBox(BlackBox):
    def set_travel_mode(self, min):
        print(f"{min}분동안 여행모드 ON")


b1 = BlackBox(20000, "까망이")
b2 = TravelBlackBox(20000, "까망이")

# b1.set.travel_mode(20)  # error
b2.set_travel_mode(20)
