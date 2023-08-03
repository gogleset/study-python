today = "일요일"

# if 조건문:
# 들어쓰기 실행문
# else 조건문:
# 들여쓰기 실행문

if today == "일요일":
    print("게임 한 판")  # true
else:
    print("공부시작")  # false


# elif 아니라고? 이건 어떄 else

if today == "일요일":
    print("일요일")
elif today == "토요일":
    print("토요일")
else:
    print("주중")
