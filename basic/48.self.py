class BlackBox:
    # self는 함수를 호출할떄도 불리지 않는다.
    # self는 객체 자기 자신을 가리킨다
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def print_self(self, min):
        print(f"나의 주소는 {self}")
        print(f"나의 이름은 {self.name}")
        print(f"나의 가격은 {self.price}")
        print(f"여행모드 {min}분 ON")


b1 = BlackBox(20000, "메롱이")
b2 = BlackBox(30000, "야옹이")
b1.print_self(20)  # BlackBox.print_self(b1, 20)과 같은 말

b2.print_self(20)

# 각자의 저장된 위치가 달라 다른 객체임을 알 수 있다.

# 클래스 메소드를 정의할 때 처음 전달값은 반드시 self
# 메소드 내에서는 self.name 과 같은 형태로 멤버변수를 사용한다.
