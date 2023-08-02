my_list = ["오예스", "몽쉘", "초코파이"]  # 순서보장!
your_list = [1, 2, 3.14, True, False, "아무거나"]

print(my_list[0])  # 오예스
print(my_list[0:2])  # 오예스 몽쉘
print("몽쉘" in my_list)  # True or False
print(len(my_list))  # 3

# 값 수정
my_list[1] = "몽쉘카카오"
print(my_list)
my_list.append("ㅎㅎ")  # 맨뒤값넣기
print(my_list)
my_list.remove("오예스")  # 값 삭제
my_list.extend(your_list)
print(my_list)
