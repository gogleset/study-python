# 에러의 원인 출력
num1 = 3
num2 = 0
try:
    # 수행 문장
    result = num1 / num2
    # num1 = 3, num2 = 0 이라고 가정
    print(f"연산 결과는 {result}입니다 ")
except TypeError:
    print("값의 형태가 이상해요")
except ZeroDivisionError:  # 값이 0일때
    print("0으로 나눌 수 없어요")
except Exception as err:  # Exception으로 error의 정확한 원인을 찾을 수 있음
    # 에러 발생 시 수행 문장
    print("에러가 발생했습니다.")
    print(err)
else:
    print("정상 동작했습니다")
    # 정상 동작 시 수행 문장
finally:
    print("수행 종료")
    # 마지막으로 수행할 문장
