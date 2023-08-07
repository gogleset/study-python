# open(파일명, 열기모드, encoding='인코딩')

f = open("list.txt", "w", encoding="utf-8")  # 쓰기모드로 파일 열기
f.write("김xx\n")
f.write("최xx\n")
f.write("안xx\n")
f.write("유xx\n")

f.close()  # 반드시 닫기
# list.txt가 없다면 새로 만들고 있다면 덮어쓰기


f = open("list.txt", "r", encoding="utf-8")  # 읽기모드로 파일 열기
# 한줄씩 출력
for line in f:
    print(line, end="")  # end로 불필요한 줄 제거

contents = f.read()
print(contents)
f.close()  # 반드시 닫기
