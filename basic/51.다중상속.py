# 다중 상속
class BlackBox:
    def __init__(self, price, name):
        self.price = price
        self.name = name


class VideoMaker:
    def make(self):
        print("추억용 영상 제작")


class MailSender:
    def send(self):
        print("메일 전송")


# 다중상속은 그냥 콤마로 하면 됨
class TravelBlackBox(BlackBox, VideoMaker, MailSender):
    def __init__(self, price, name, sd):
        super().__init__(price, name)
        self.sd = sd

    def set_travel_mode(self, min):
        print(f"{min}분동안 여행모드 ON")


b1 = TravelBlackBox(20000, "DM-123", "64GB")
b1.make()
b1.send()
