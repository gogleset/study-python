# return 문을 작성하여 반환함


def get_price():
    return 20000


print(get_price())


def set_price(params):
    if params == "단골":
        return 10000
    else:
        return 13000


print(set_price("단골1"))
