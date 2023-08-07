# 개수가 바뀔 수 있는 파라미터 (전달값이 몇개인지 모를때)
# 파라미터 앞에 *찍기
# 파라미터에 마지막 순서로 하나만 넣을 수 있다


def visit(today, *customers):
    print(today)
    # 가변인자로 받은 값들 출력
    for customer in customers:
        print(customer)


visit("monday", "asd", "asd1", "asd12", "Asd123")
