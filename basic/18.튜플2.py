my_tuple = ("오예스", "몽쉘", "초코파이")  # 패킹
(pie1, pie2, pie3) = my_tuple  # 언패킹 자바스크립트 구조분해 할당이랑 똑같음

print(pie1, pie2, pie3)

# *을 적어주면 나머지가 할당되고 튜플이 아니라 리스트형태임
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
(one, two, *others) = numbers
print(one, two)
print(*others)

(*others, nine, ten) = numbers
print(nine, ten)
print(*others)

(one, *others, ten) = numbers
print(one, ten)
print(*others)
