snack = "꿀꽈배기"
two = "2개"

juseyo = snack + two
# 꿀꽈배기2개
juseyo += "주세요"  # 로도 가능
# 숫자도 마찬가지

num = 3
num = num + 2
num += 2  # 위 문장과 같다

num -= 1  # 빼고 할당
num *= 2  # 곱하고 할당
num /= 4  # 나누고 할당

print(num)

# 길이
print(len(snack))  # len 함수는 문자의 길이를 나타낸다.

# 여러줄 문자 """로 감싸주면됨
snack = """꿀꽈배기는
너무
맛있어요
"""
