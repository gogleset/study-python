# 튜플은 수정 불가라 하는데 바꿀 수 있다!!! ㄴㅇㄱ

my_tuple = ("오예스", "몽쉘")
my_list = list(my_tuple)
my_list.append("초코파이")
my_tuple = tuple(my_list)  # 리스트와 튜플은 이런식으로 형변환 할 수 있다.

# 리스트는 중복값이 허용되지만, 세트는 허용되지 않는다
my_list = ["오예스", "몽쉘", "초코파이", "초코파이", "초코파이"]
my_list = set(my_list)  # 세트 형 변환
my_list = list(my_list)  # 다시 리스트로 형변환, 순서는 뒤죽박죽
print(my_list)

my_list = ["오예스", "몽쉘", "초코파이", "초코파이", "초코파이"]
print(my_list)
my_dic = dict.fromkeys(my_list)  # 딕셔너리의 키로 설정하는 메소드 값은 모두 None
print(my_dic)
my_list = list(my_dic)
print(my_list)  # 순서가 보장된 중복값을 지운 배열값으로 변환된다.
