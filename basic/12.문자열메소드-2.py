s = "나도 고등학교"

print(s.startswith("나도"))  # ~로 시작하는지
print(s.endswith("나도"))  # ~로 끝나는지
print(s.strip())  # 앞뒤불필요한부분제거 아무것도 안넣으면 앞뒤 공백제거
print(s.replace("나도", "너도"))  # 단어 바꾸기
print(s.find("고등"))  # 단어 위치 찾기
print(s.center(10, "-"))  # 다른 문자들 사이 가운데 (총길이, 바꿀character)
