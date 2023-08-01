python = "파이썬"
java = "자바"

print(python, java)  # 콤마로 구분지을 수 있음
# 문장 속에 넣으려면?
# 개발 언어에는 파이썬 자바가 있어요. 같은 문장이라면?
print("개발 언어에는 " + python + ", " + java + "가 있어요.")

# 1. { } + format
print("개발 언어에는 {}, {} 등이 있어요".format(python, java))
# format에 나열한 순서대로 들어감
# 2. {N} + format
print("개발 언어에는 {0}, {1} 등이 있어요".format(python, java))
print("개발 언어에는 {1}, {0} 등이 있어요".format(python, java))
# format에 나열한 숫자 순서대로 들어감

# 3. f-string
print(f"개발 언어에는 {python}, {java} 등이 있어요")
