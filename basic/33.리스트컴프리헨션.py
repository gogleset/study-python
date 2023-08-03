product = ["gg-123", "gg-456", "zz-123", "zz-456"]
## zz모델만 리콜
recall = []

for p in product:  # product 배열 순회
    if p.startswith("zz"):  # 원소 내용 조회
        recall.append(p)  # 맞으면 recall대상에 넣어주기

print(recall)

# List Comprehension으로 저 3줄을 간단히 할 수 있음
# 리스트 내에서 어떤 조건에 해당하느 데이터를 뽑아내거나 값을 바꿔서 새로운 리스트를 만들 때 사용가능

# new_list = [변수 활용 for 변수 in 반복대상 if 조건]

my_list = [1, 2, 3, 4, 5]
new_list = [x for x in my_list if x > 3]
print(new_list)
new_list = [x + 1 for x in my_list if x > 3]
print(new_list)
new_list = [x * 2 for x in my_list if x > 3]
print(new_list)
new_list = [str(x + 2) + "일" for x in my_list if x > 3]
print(new_list)
# 맨 처음 x의 값을 커스터마이징할 수 있고 결국 x의 값을 리턴해서 리스트 해준다고 생각하면됨


new_recall = [x for x in product if x.startswith("zz")]
print(new_recall)

# 다양한 사용법들
new_recall = [str(x) + "zz" for x in product if x.startswith("zz")]
print(new_recall)
new_recall = [x.upper() for x in product]
print(new_recall)
