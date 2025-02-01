    # 숫자 자료형------------------------------------------------
print(5)        #print 안에 있는 문자를 그대로 출력
print(5+3)      #덧셈 가능
print(2*3)      #곱셉은 "*"사용
    #문자열 자료형-----------------------------------------------
print("풍선")   #문자형은 ""또는''사용
print("ㅋ"*9)   #문자뒤에 숫자곱해 사용가능
    #boolean 자료형(참/거짓)-------------------------------------
print(5 > 10)   #5는 10보다 작음으로 거짓 false가 출력
print(5 < 10)   #5는 10보다 작음으로 참 true가 출력
print(True)     #print에 직접 true or false를 넣어도 출력 가능
print(False)
print(not True) #not 사용시 뒤에있는 문장의 반대로 출력 예)not True -> False
    #변수---------------------------------------------------------
#요청: 애완동물을 소개해주세요

name = "연탄이"
animal = "강아지"   #--> 변수 선언후 값적기 문자형은 따옴표로 감싸고 정수형은 안감쌈
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요.")
print(name + "는 " + str(age) + "살이며," + hobby + "을 아주 좋아해요") #->정수형을 변수로 쓰기위해 str(정수형변수)로 감싸야함
print(name + "는 어른일까요? " + str(is_adult))   #boolean형도 str(boolean)로 감싸야함
    #연산자---------------------------------------------------------
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # X**Y X의 Y제곱
print(5%3)  # 5/3의 나머지
print(5//3) #5/3의 몫

print(10 > 3) # True
print(4 >= 7) #4는 7보다 크거나같다 False

print(3 == 3) #3과3은 같다 True
print(4 == 2) #4는 2와 같다 False

print(1 != 3) #1과3은 같지 않다 True
print(not(1 != 3)) #not을 붙였으므로 True의 반대인 False가 출력

print((3 > 0) and (3 < 5)) #앞항과 뒤향 모두 만족해야 True 출력 True
print((3 > 0) & (3 < 5)) #앞항과 뒤향 모두 만족해야 True 출력 True

print((3 > 0) or (3 > 5)) #둘중 하나의 항이라도 만족시 True 출력 2번항이 틀렸지만 1번항이 만족하므로 True 출력
print((3 > 0) | (3 > 5)) #둘중 하나의 항이라도 만족시 True 출력 2번항이 틀렸지만 1번항이 만족하므로 True 출력

print(5 > 4 > 3) #True
print(5 > 4 > 7) #False
    #간단한 수식--------------------------------------------------------
print(2 + 3 * 4) #14
print((2 + 3) * 4) #20

number =2 + 3 * 4 #14
print(number) #14

number = number+2 #변수의 X를 더하고 싶을때 사용
print(number) #16

number += 2 #변수의 X를 더하고 싶을때 사용(위의 number = number+2와 같음)
print(number) #18

number *= 2 #변수의 X를 곱하고 싶을때 사용
print(number) #36

number /= 2 #변수의 X를 나누고 싶을때 사용
print(number) #18

number -= 2 #변수의 X를 뺴고 싶을때 사용
print(number) #16

number %= 2 #변수의 나머지를 구할때 사용
print(number) #0
    #숫자 처리 함수------------------------------------------------------------
print(abs(-4)) #4
#abs후 괄호안에 숫자를 넣으면 절대값을 구할수있음

print(pow(4, 2)) #16
#pow(x,y)는 x의y승 x의y제곱    

print(max(5,12)) #12
#괄호안의 수중에서 가장 큰 수를 찾아줌

print(min(5,12)) #5
#괄호안에 수중에서 가장 작은 수를 찾아줌

print(round(3.14)) #3
#괄호안의 숫자를 반올림함

from math import * #math 라이브러리에 있는 모든 기능을 이용하겠다(아래 코드는 라이브러리 개방후 사용가능)
print(floor(4.99)) #4
#괄호안의 숫자를 내림

print(ceil(3.14)) #4
#괄호안의 숫자를 올림

print(sqrt(16)) #4
#괄호안 숫자의 제곱근 구하기
    #랜덤함수-----------------------------------------------------------------------
from random import * #랜덤 라이브러리 사용

print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성

print(random() * 10) #0.0 ~10.0 미만의 임의의 값 생성

print(int(random() * 10)) #int 사용시 0 ~10 미만의 임의의 값 생성

print(int(random() * 10) + 1) #1 ~ 10 이하의 임의의 값 생성

print(randrange(1, 45)) #1 ~ 45 미만의 임의의 값 생성(이하로 바꿀시 45위치의 숫자의 1를 더하면됨)

print(randint(1, 45)) #1 ~ 45 이하의 임의의 값 생성
    #문자열--------------------------------------------------------------------------
sentence = '나는 소녀입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,          
파이썬은 쉬워요             
"""
#"""문자""" 사용시 줄바꿈 가능
print(sentence3)
    #슬라이싱----------------------------------------------------------------------------
jumin = "111019-1234567"

print("성별 :" + jumin[7]) #원하는 값을 얻기위해 []사용,1부터세는게 아닌 0부터 세야함
print("연 :" +jumin[0:2])  #0:2 == 0부터 2직전(그니까 1)위치의 값출력
                           #0,1 위치에 값을 얻으려면 0:1이아닌 0:2 한자리올려 사용
print("월 :" + jumin[2:4])
print("일 :" + jumin[4:6])
print("생년월일" + jumin[:6]) #0부터 시작시 0을 생략해도됨
print("뒤 7자리 :" + jumin[7:]) #끝도 생략 

print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) #뒤에 부터 할꺼면 맨뒤가 -1로됨 즉 이식에선 7 == -1
    #문자열처리함수------------------------------------------------------------------------
python = "Python is Amazing"
print(python.lower()) # .lower() 사용시 모든 문자가 소문자로 출력
print(python.upper()) # .upper() 사용시 모든 문자가 대믄자로 출력
print(python[0].isupper()) #python의 0번째 문자가 대문자 인가? True
print(len(python)) #len() 사용시 문자의 길이 반환

print(python.replace("Python", "Java"))
#python 변수 안에서 "Python" 이란 문자를 "Java"로 교체해 춮력

index = python.index("n") #python이란 변수에서 n이 몇번쨰에 위치되어있는지 출력
print(index) 

index = python.index("n", index + 1) #앞에 찾았던 위치 다음부터 찾기(2번째 n 찾기)
print(index)

print(python.find("n")) #n찾기

#중요________________________________________________________

# print(python.find("Java"))  # -> 원하는 값이 없을시 -1출력  ==원하는 값이 원으면 -1출력 프로그램 진행
# print(python.index("Java")) # -> 원하는값이 없으면 오류가남 ==원하는 값이 없으면 오류가 뜨며 프로그램 종료
#____________________________________________________________
print(python.count("n")) #변수에서 n이 몇번 나왔는지 출력
    #문자열포멧------------------------------------------------------------------------------
print("a" + "b") #ab
print("a","b")   #a b
#방법 1
print("나는 %d살 입니다" % 20) #d == 정수
print("나는 %s를 좋아해요" % "파이썬") #s == 다 사용 가능
print("Apple은 %c로 시작해요" %"A")   #c == 단수만 ㄱㄴ

print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))
#방법 2
print("나는 {}살 입니다" .format(20)) #.format()안에 있는 값을 {}에 집어넣기
print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간")) # {}안에 숫자를 넣으면 순서 지정 가능
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))
#방법 3
print("나는 {age}살이며,{color}색을 좋아해요" .format(age = 20,color = "빨간")) 
#format에 있는값을 {} 변수처럼 활용가능
#방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며,{color}색을 좋아해요") #f를 쓰면 외부 변수 사용 가능
    #틸출문제---------------------------------------------------------------------------------
print("백문이 불여일견 \n백견이 불여일타") #\n :줄바꿈

print("저는 \"나도코딩\"입니다") #문장안에서 "" 사용하려면 \"식으로 사용

#\\: 문장내에서 \하나로 출력

print("Red Apple\rPine") # \r: 커서를 맨앞으로이동

print("Redd\bApple") # \b : 백스페이스 (한글자 삭제)

print("Red\tApple") #\t : 탭 
    #리스트-------------------------------------------------------------------------------------
# 지하철 칸 별로 10,20,30
subway = 10
subway2 = 20
subway3 = 30

subwayzero = [10, 20, 30] #리스트를 사용해 비슷한것을 하나로 묶어줌

subwayzero = ["유재석", "조세호", "박명수"]
print(subwayzero)

#조세호가 몇번째 칸에 타고있는가?
print(subwayzero.index("조세호")) # 1번째

#하하가 다음 정류정에서 다음 칸에 탐
subwayzero.append("하하") #append == 맨뒤에 추가
print(subwayzero)

#정형돈이 유재석/조세호 사이에 탐
subwayzero.insert(1, "정형돈") #(추가할 위치, 추가할 사람)
print(subwayzero)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subwayzero.pop()) #맨뒤 사람을 한명씩 꺼냄
print(subwayzero)       #여러번 써서 여러명을 꺼낼수있음

#같은 이름을 가진사람이 몇명인지 확인하기
subwayzero.append("유재석") # ->유재석을 2명으로 만들기
print(subwayzero)
print(subwayzero.count("유재석"))  #-> 유재석이 몇명인지 세기

#정렬도 ㄱㄴ
number_list = [5,2,4,3,1]
number_list.sort() #sort ==정렬한다는 의미
print(number_list) 

#순서 뒤집기 ㄱㄴ
number_list.reverse() #12345를 54321로 바꾸기
print(number_list)

#모두 지우기
number_list.clear()
print(number_list)

#다앵한 자료형과 함께사용
number_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장
number_list.extend(mix_list)
print(number_list)
    #사전-----------------------------------------------------------------------------------------
cabinet = {3:"유재석", 100:"김태호"} # (key : value)
print(cabinet[3])  
#할당되지않은 수를 괄호에 적으면 오류가 나며 프로그램이 종료됨

print(cabinet.get(100))
#None 출력 후 프로그램이 게속 진행됨

print(cabinet.get(1, "사용 가능")) 
#할당되지않은 값 뒤에 뭔갈 붙여 None이 아닌 다른 문자 출력 가능

print(3 in cabinet)
# True  | 3이란 키가 있는가?

print(6 in cabinet)
# False | 5라는 키가 있는가

cabinet = {"A-3":"유재석", "B-100":"김태호"} 
#key가 문자형이여도됨

        #새손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호" # 새로운값이면 추가, 원래 있던 값은 업데이트
print(cabinet)

        #간손님
del cabinet["A-3"] #del로 원하는 key 삭제 가능
print(cabinet)     

        #key 들만 출력
print(cabinet.keys()) #무슨 key가 있는지 알려줌

        #value 들만 출력
print(cabinet.values()) #무슨 value가 있는지 알려줌

        #key,value 쌍으로 출력
print(cabinet.items())

        #모든 값 삭제
cabinet.clear()
print(cabinet)
    #튜플------------------------------------------------------------------------------------
#내용 변경,추가 불가능 /list보다 속도가 빠름
menu = ("돈가스", "치즈가스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"          
print(name, age, hobby)

#튜플 이용시 위 코드를 한번에 출력 ㄱㄴ
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
    #세트-------------------------------------------------------------------------------------
# 집합(set)
# 중복 안됨, 순서 업음
my_set = {1,2,3,3,3}
print(my_set) #중복은 하나만 출력됨

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 (java와 pythin을 모두 할수있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (java도 할수있거나 python도 할수있는 개발자)
print(java | python)  
print(java.union(python))

#차집합 (java는 할수있지만, python은 할줄 모르는 개발자
print(java - python)
print(java.difference(python))

#python을 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)
