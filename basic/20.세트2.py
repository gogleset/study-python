# 세트는 값의 순서가 보장되어 있지 않기 때문에 인덱스로 접근할 수 없다. 그렇다고 수정이 불가한 건 아니다

# 추가
my_set = {"돈가스", "보쌈", "제육덮밥"}
my_set.add("닭갈비")
print(my_set)

# 삭제
my_set.remove("보쌈")
print(my_set)

# 값을 모두 삭제
my_set.clear()
print(my_set)

# 이 세트자체를 삭제
# del my_set
# print(my_set)

# copy() 세트 복사
# discard() 값 삭제
# isdisjoint() 두 세트에 겹치는 값이 없는지 여부
# issubset() 다른 세트의 부분집합인지 여부
# issuperset() 다른 세트의 상위집합인지 여부
# update() 다른 세트의 값들을 더함
