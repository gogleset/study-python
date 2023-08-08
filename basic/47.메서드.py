class BlackBox:
    # 생성자 함수 만들기, 객체가 생성될때 자동으로 실행해줌
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def set_travel_mode(self, min):
        print(f"{min}분동안 여행모드 ON")


b1 = BlackBox(20000, "까망")
b1.set_travel_mode(20)  # console 출력
