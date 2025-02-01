    #퀴즈1번---------------------------------------------------
# station = "사당"
# print(station + "행 열차가 들어오고있습니다")
# station = "신도림"
# print(station + "행 열차가 들어오고있습니다")
# station = "인천공항"
# print(station + "행 열차가 들어오고있습니다")
    #퀴즈2번---------------------------------------------------
# from random  import *

# date = randint(4, 28)
# print("오프라인 스터디 모임날짜는 매월" + str(date) + "일로 선정되었습니다")
    #퀴즈3번---------------------------------------------------
site = "http://naver.com"
asdf = site.replace("http://","") #naver.com
hjkl = asdf.replace(".com","") #naver
qwer = hjkl.replace("er","") #nav
count = len(hjkl)
count2 = hjkl.count("e")
good = "!"

print(f"생성된 비밀번호 : {qwer}{count}{count2}{good}")

