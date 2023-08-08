class BlackBox:
    def __init__(self, price, name):
        self.price = price
        self.name = name


# super를 통한 부모 클래스의 인스턴스에 값을 추가하기
class TravelBlackBox(BlackBox):
    def __init__(self, price, name, sd):
        # BlackBox.__init__(self, price, name) 이것도 가능하지만
        # super로 부모 클래스 메소드 호출
        super().__init__(price, name)
        self.sd = sd

    def set_travel_mode(self, min):
        print(f"{min}분동안 여행모드 ON")
