drama = ["시즌1", "시즌2", "시즌3", "시즌4"]

for x in drama:
    print(x)
    if x == "시즌3":
        print("재미없대 그만보자")
        break  # 반복문 탈출
    print(f"{x}시청")
