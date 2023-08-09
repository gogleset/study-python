# 예외처리
num1 = 3
num2 = 0
try:
    # 수행 문장
    result = num1 / num2
    # num1 = 3, num2 = 0 이라고 가정
    print(f"연산 결과는 {result}입니다 ")
except:
    # 에러 발생 시 수행 문장
    print("에러가 발생했습니다.")
else:
    print("정상 동작했습니다")
    # 정상 동작 시 수행 문장
finally:
    print("수행 종료")
    # 마지막으로 수행할 문장
