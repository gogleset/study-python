# default value를 정할 수 있다.


def set_price(params="단골아님"):
    if params == "단골":
        return True
    else:
        return False


print(set_price())
