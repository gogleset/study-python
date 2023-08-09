import xlwings  # 엑셀 관련 패키지

# 1. 설치된 패키지 목록보기
# $ pip3 list

# 2. 가상환경 만들기
# $ python -m venv 가상환경env이름

# 3. 가상환경 들어가기
# $ source 가상환경env이름/bin/activate

# 4. 가상환경에 설치된 패키지 확인하기
# $ pip3 list

# 5. 가상환경에 패키지 설치하기
# $ pip3 install 패키지이름
print(xlwings.__version__)
 