# 조건이 참인 동안에 실행

max = 25  # 최대 허용 무게
weight = 0  # 현재 캐리어 무게
item = 3  # 각 짐의 무게

while weight + item <= max:  # 캐리어에 짐을 더 넣어도 되는지 확인
    weight += item
    print("짐을 추가합니다")
print(f"총 무게는 {weight}입니다")
