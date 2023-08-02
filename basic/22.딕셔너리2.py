# key value
# 딕셔너리 = {key1: value, key2: value } 걍 object
person = {
    "이름": "gogleset",
    "나이": 7,
    "키": 123,
}
print()
# print(person["별명"])  # error 값이 없기때문
print(person.get("별명"))  # 없는 키값에 접근해도 error 대신 None 출력

# 값 추가
person["별명"] = "choiTrue"
print(person)
# 값 수정
person["키"] = 130  # 그냥 똑같이 해주면 됨
print(person)
# 여러 값 수정
person.update({"키": 130, "나이": 8})
print(person)

# 특정 키: 값 삭제
person.pop("별명")
print(person)

# 모든 값 삭제
# person.clear()
# print(person)

# 어떤 키들이 존재?
print(person.keys())
# 어떤 값들이 존재?
print(person.values())
# 걍 다 출력해
print(person.items())
