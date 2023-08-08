class BlackBox:
    def __init__(self, price, name):
        # 멤버변수
        self.price = price
        self.name = name


# b1, b2는 같은 값을 주었다고 해서 같은 객체일까?
# 결론만 얘기하면 아니다. 다른 독립적인 인스턴스이다.
b1 = BlackBox(2000, "까망이")
b2 = BlackBox(2000, "까망이")
# 멤버변수 추가
b1.nickname = "1"
print(b1.nickname)
# print(b2.nickname) # b2에는 nickname이 없으니 증명완료
