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


class TravelBlackBox(BlackBox, VideoMaker, MailSender):
    def __init__(self, price, name, sd):
        super().__init__(price, name)
        self.sd = sd

    def set_travel_mode(self, min):
        print(f"{min}분동안 여행모드 ON")


class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, min):  # 부모 메서드 재정의
        print(f"{min}분동안 여행모드 ON")
        self.make()
        self.send()


# 자식 클래스에서 같은메소드를 새로 정의하지 않으면? 부모 클래스의 메소드를 쓰고, 자식클래스에서 같은 메소드를 새로 정의하면? 자식 클래스의 메소드를 쓴다.
