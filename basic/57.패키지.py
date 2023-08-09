# 호출
import package.goodbye  # package 폴더의 goodbye를 호출

# 뽑아서 호출
from package.goodbye import bye

# 다중 import
from package import goodbye, goodjob

goodjob.say()
goodbye.bye()
