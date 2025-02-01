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
 








