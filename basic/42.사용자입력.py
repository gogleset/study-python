# input으로 사용자 입력받을 수 있음 문자열로만받음

name = input("예약자분 성함이 뭐에용?")
# 입력한 값이 name에 저장됨
print(name)
customer = int(input("몇명이세요"))
# 입력한 값이 name에 저장됨
print(customer)
if customer > 4:
    print("8인실로 안내해드릴게요")
elif customer > 2:
    print("4인실로 안내해드릴게요")
else:
    print("2인실로 안내해드릴게요")
