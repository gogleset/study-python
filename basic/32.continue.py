drama = ["시즌1", "시즌2", "시즌3", "시즌4", "시즌5"]

for x in drama:
    print(x)
    if x == "시즌3":
        print("재미없어")
        continue  # 동작 건너뛰기 바로 처음으로 건너뜀
    print("시청")
