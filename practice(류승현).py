# 문제 1
"""
print("Hello World")
"""


#문제 2
"""
print("Mary's cosmetics")

"""

#문제 3
"""
print('신씨가 소리질렀다. "도둑이야".')

"""

#문제 4

"""
print('"C:\Windows"')
"""

#문제 5
"""
print('"안녕하세요.\n 만나서\t\t 반갑습니다."')
"""
# \n은 줄바꿈, \t는 텝


#문제 6
"""
print("오늘은", "일요일")
"""
# 출력결과 : 오늘은 일요일


#문제 7
"""
print("naver;kakao;sk;samsung")
"""

"""
print("naver", "kakao", "sk", "samsung", sep=";")
"""

#문제 8
"""
print("naver/kakao/sk/samsung")
"""
"""
print("naver", "kakao", "sk", "samsung", sep="/")
"""

#문제 9
"""
print("first", end="");print("second")
"""

#문제 10
"""
print(5/3)
"""

#문제 11
"""
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)
"""

#문제 12
"""
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액)
print(현재가)
print(PER)
"""

#문제 13
"""
s = "hello"
t = "python"
print(s+"!", t)
"""

#문제 14
"""
print(2 + 2 * 3)
"""

#문제 15
"""
a = "132"
print(type(a))
"""

#문제 16
"""
num_str = "720"
num_int = int(num_str)
print(num_int,type(num_int))
"""

#문제 17
"""
num = 100
str = str(num)
print(str,type(str))
"""

#문제 18
"""
a = "15.79"
float = float(a)
print(float,type(float))
"""

#문제 19
"""
year = "2020"
int_year = int(year)
print(int_year-3,type(int_year-3))
print(int_year-2,type(int_year-2))
print(int_year-1,type(int_year-1))
"""

#문제 20
"""
월금액 = 48584
무이자 = 36
총금액 = 월금액 * 무이자
print(총금액)
"""

#문제 21
"""
letters = 'python'
print(letters[0], letters[2])
"""

#문제 22
"""
license_plate = "24가 2210"
print(license_plate[-4:])
"""

#문제 23
"""
string = "홀짝홀짝홀짝"
print(string[::2])
"""

#문제 24
"""
string = "PYTHON"
print(string[::-1])
"""

#문제 25
"""
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
"""

#문제 26
"""
phone_number = "010-1111-2222"
print(phone_number.replace("-",""))
"""

#문제 27
"""
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[1])
"""

#문제 28
"""
lang = 'python'
lang[0] = 'p'
print(lang)
"""

#문제 29
"""
string = 'abcdfe2a354a32a'
string1 = string.replace('a','A')
print(string1)
"""

#문제 30
"""
string = 'abcd'
string.replace('b', 'B')
print(string)
"""

#문제 31
"""
a = '3'
b = '4'
print(a + b)
"""

#문제 32
"""
print("Hi" * 3)
"""

#문제 33
"""
print('-' * 80)
"""

#문제 34
"""
t1 = 'python'
t2 = 'java'
print((t1 + ' ' + t2 + ' ') * 4)
"""

#문제 35
"""
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 : %d" %(name1,age1))
print("이름 : %s 나이 : %d" %(name2,age2))
"""

#문제 36
"""
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : {} 나이 : {}" .format(name1,age1))
print("이름 : {} 나이 : {}" .format(name2,age2))
"""

#문제 37

"""
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")
"""

#문제 38
"""
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",","")
int_상장주식수 = int(컴마제거)
print(int_상장주식수, type(int_상장주식수))
"""

#문제 39
"""
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])
"""

#문제 40
"""
data = "   삼성전자   "
new_data = data.strip()
print(new_data)
"""

#문제 41
"""
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)
"""

#문제 42
"""
ticker = "BTC_KRW"
ticker1 = ticker.lower()
print(ticker1)
"""

#문제 43
"""
a = "hello"
a= a.capitalize()
print(a)
"""

#문제 44
"""
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx")) #파일 이름이 xlsx로 끝나는가?
"""

#문제 45
"""
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx","xls")))
"""

#문제 46
"""
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))
"""

#문제 47
"""
a = "hello world"
print(a.split(" "))
"""

#문제 48
"""
ticker = "btc_krw"
print(ticker.split("_"))
"""

#문제 49
"""
date = "2020-05-01"
print(date.split("-"))
"""

#문제 50
"""
data = "039490    "
print(data.rstrip())
"""

#문제 51
"""
movie_rank = ["닥터스트레인지", "스플릿", "럭키"]
print(movie_rank)
"""

#문제 52
"""
movie_rank = ["닥터스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)
"""

#문제 53
"""
movie_rank = ["닥터스트레인지", "스플릿", "럭키", "배트맨"]
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)
"""

#문제 54
"""
movie_rank = ["닥터스트레인지", "스플릿", "럭키", "배트맨"]
del movie_rank[3]
print(movie_rank)
"""

#문제 55
"""
movie_rank = ["닥터스트레인지", "슈퍼맨", "스플릿", "배트맨"]
del movie_rank[2]
del movie_rank[2]
print(movie_rank)
"""

#문제 56
"""
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang3 = lang1 + lang2
print(lang3)
"""

#문제 57
"""
nums = [1, 2, 3, 4, 5, 6, 7]
print("max : ",max(nums))
print("min : ",min(nums))
"""

#문제 58
"""
nums = [1, 2, 3, 4, 5]
print(sum(nums))
"""

#문제 59
"""
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
"""

#문제 60
"""
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)
"""

#문제 61
"""
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
"""

#문제 62
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
"""

#문제 63
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])
"""

#문제 64
"""
nums = [1, 2, 3, 4, 5]
print(nums[::-1])
"""

#문제 65
"""
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])
"""

#문제 66
"""
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))
"""

#문제 67
"""
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))
"""

#문제 68
"""
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))
"""

#문제 69
"""
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)
"""

#문제 70
"""
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
"""

#문제 71
"""
my_variable = ()
print(my_variable,type(my_variable))
"""

#문제 72
"""
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)
"""

#문제 73
"""
my_tuple = (1,)
print(my_tuple, type (my_tuple))
"""

#문제 74
"""
t = (1, 2, 3)
t[0] = 'a'
"""

#문제 75
"""
t = 1, 2, 3, 4
print(t)
"""

#문제 76
'''
t = ('a', 'b', 'c')
t = 'A', 'b', 'c'
print(t)
'''

#문제 77
"""
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
"""

#문제 78

"""
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
"""

#문제 79
"""
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
"""

#문제 80
"""
data = tuple(range(2, 99, 2))
print( data )
"""

#문제 81
"""
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b= scores
print(valid_score)
"""

#문제 82
"""
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)
"""

#문제 83
"""
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b = scores
print(valid_score)
"""

#문제 84
"""
temp = { }
print(temp)
"""

#문제 85
"""
ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(ice)
"""

#문제 86
"""""
ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
ice["죠스바"] = 1200
ice["월드콘"] = 1500
print(ice)
"""

#문제 87
"""
ice = {'메로나': 1000, '폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
print("메로나 가격 :", ice['메로나'])
"""

#문제 88
"""
ice = {'메로나': 1000, '폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
ice['메로나'] = 1300
print(ice['메로나'])
"""

#문제 89
"""
ice = {'메로나': 1000, '폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
del ice['메로나']
print(ice)
"""

#문제 90
"""
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream['누가바']
"""

#문제 91
"""
inventory = {"메로나": [300, 20], 
             "비비빅": [400, 3], 
             "죠스바": [250, 100]}
print(inventory)
"""

#문제 92
"""
inventory = {"메로나": [300, 20],
             "비비빅": [400, 3],
             "죠스바": [250, 100]}
print(inventory["메로나"][0], "원")
"""

#문제 93
"""
inventory = {"메로나": [300, 20],
             "비비빅": [400, 3],
             "죠스바": [250, 100]}
print(inventory["메로나"][1], "개")
"""

#문제 94
"""
inventory = {"메로나": [300, 20],
             "비비빅": [400, 3],
             "죠스바": [250, 100]}
inventory["월드콘"] = [500,7]
print(inventory)
"""

#문제 95
"""
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys())
print(ice)
"""

#문제 96
"""
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
price = list(icecream.values())
print(price)
"""

#문제 97
"""
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
total = sum(icecream.values())
print(total)
"""

#문제 98
"""
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
"""

#문제 99
"""
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals))
print(result)
"""

#문제 100
"""
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)
"""

#문제 101
"""
bool 자료형
"""

#문제 102
"""
print(3 == 5) # ==연산자는 같음을 비교
"""

#문제 103
"""
print(3 < 5)
"""

#문제 104
"""
x = 4
print(1 < x < 5) # 1 < 4 < 5
"""

#문제 105
"""
print ((3 == 3) and (4 != 3)) # 3과 3이 같고 4와 3이 다른가
"""

#문제 106
"""
print(3 => 4) # 연산자 기호가 잘못 됨. 3 >= 4가 옳은 표현
"""

#문제 107
"""
if 4 < 3:
    print("Hello World") # 조건이 만족하지 않았기 때문에 출력X
"""

#문제 108
"""
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.") # 조건이 만족하지 않았으므로 else의 값 출력
"""

#문제 109
"""
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")       # 비교 조건이 없으므로 True값 출력 & print("4") 출력
"""

#문제 110
"""
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")         # 비교조건이 없으므로 True값 출력(3) &  print("5") 출력
"""

#문제 111
"""
user = input("입력:")
print(user * 2)
"""

#문제 112
"""
num = input("숫자를 입력하시오:")
print(int(num) + 10)              # 입력값은 문자형이므로 정수형으로 변경시켜주어야 한다!!
"""

#문제 113
"""
num = input("숫자를 입력하시오:")
if int(num)%2 == 0 :
    print("짝수")
else :
    print("홀수")
"""

#문제 114
"""
num = input("입력값 :")
if int(num) + 20 <= 255 :
    print(" 출력값 : %d" %(int(num)+20))
else :
    print("출력값 : 255")
"""

#문제 115
"""
num = input("입력값 :")
if 0 <= (int(num) - 20) <=255 :
    print("출력값 : %d" %(int(num)-20))
elif (int(num) - 20) < 0 :
    print("출력값 : 0")
else :
    print("출력값 : 255")
"""

#문제 116
"""
time = input("현재시간: ")
if time[-2:] == "00":        # 입력값의 뒤에서 두자리 판별
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")  
"""

#문제 117
"""
fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은? : ")
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")
"""

#문제 118
"""
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
result = input("종목명 : ")
if result in warn_investment_list :
    print("투자 경고 종목입니다")
else :
    print("투자 경고 종목이 아닙니다")
"""

#문제 119
"""
fruits = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
fruit = input("제가 좋아하는 계절은 : ")
if fruit in fruits:
    print("정답입니다.")
else:
    print("오답입니다.")
"""

#문제 120
"""
fruits = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
fruit = input("제가 좋아하는 과일은? : ")
if fruit in fruits.values() :
    print("정답입니다.")
else :
    print("오답입니다.")
"""

#문제 121
"""
result = input("알파벳을 입력하시오 : ")
if result.islower() :
    print(result.upper())
else :
    print(result.lower())
"""

#문제 122
"""
score = input("점수를 입력하시오 : ")
score = int(score)
if 100>= score > 80 :
    print("grade is A")
elif score > 60 :
    print("grade is B")
elif score > 40 :
    print("grade is C")
elif score > 20 :
    print("grade is D")
else :
    print("grade is E")
"""

#문제 123

"""
환율 = {"달러" : 1167 , "엔" : 1.096, "유로" : 1268, "위안" : 171}
money = input("입력 :")
num, currency = money.split()
print(float(num) * 환율[currency], "원")
"""

#문제 124
"""
num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)
"""

#문제 125
"""
number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]            # [0]은 나눈것 중 첫 번째 값
print(num)
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")
"""

#문제 126
"""
우편번호 = input("우편번호: ")
post = 우편번호[:3]
if post in ["010", "011", "012"]:
    print("강북구")
elif post in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")
"""

#문제 127
"""
주민번호 = input("주민등록번호: ")
num = 주민번호.split("-")[1]
if num[0] == "1" or num[0] == "3":
    print("남자")
else:
    print("여자")
"""

#문제 128
"""
주민번호 = input("주민등록번호: ")
back = 주민번호.split("-")[1]
if 0 <= int(back[1:3]) <= 8 :
    print("서울입니다.")
else:
    print("서울이 아닙니다.")
"""

#문제 129
"""
num = input("주민등록번호: ")
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
"""

#문제 130
"""
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
"""

#문제 131
"""
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)
"""

#문제 132
"""
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")
"""

#문제 133
"""
for 변수 in ["A", "B", "C"]:
  print(변수)

변수 = "A"
print(변수)
변수 = "B"
print(변수)
변수 = "C"
print(변수)
"""

#문제 134
"""
for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)

변수 = "A"
print("출력:", 변수)
변수 = "B"
print("출력:", 변수)
변수 = "C"
print("출력:", 변수)
"""

#문제 135
"""
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)

변수 = "A"
b = 변수.lower()
print("변환:", b)

변수 = "B"
b = 변수.lower()
print("변환:", b)

변수 = "C"
b = 변수.lower()
print("변환:", b)
"""

#문제 136
"""
변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)

for 변수 in ["10", "20", "30"] :
    print(변수)
"""

#문제 137
"""
print(10)
print(20)
print(30)

for 변수 in ["10", "20", "30"] :
    print(변수)
"""

#문제 138
"""
print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")

for 변수 in ["10", "20", "30"] :
    print(변수)
    print("-------")
"""

#문제 139  ---> *의견 공유*
"""
print("++++")
print(10)
print(20)
print(30)

for 변수 in ["++++", "10", "20", "30"] :
    print(변수)

print("++++")
for 변수 in [10, 20, 30]:
  print(변수)
"""

#문제 140
"""
print("-------")
print("-------")
print("-------")
print("-------")

for 변수 in [1, 2, 3, 4]:
  print("-------")
"""

#문제 141
"""
리스트 = [100, 200, 300]
for 변수 in 리스트 :
    print(변수 + 10)
"""

#문제 142
"""
리스트 = ["김밥", "라면", "튀김"]
for 변수 in 리스트 :
    print("오늘의 메뉴 : %s" %변수)
"""

#문제 143
"""
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for 변수 in 리스트 :
    length = len(변수)
    print(length)
"""

#문제 144
"""
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트 :
    length = len(변수)
    print("%s %d" %(변수, length))
"""

#문제 145
"""
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트 :
    print(변수[0])
"""

#문제 146
"""
리스트 = [1, 2, 3]
for 변수 in 리스트 :
    print("3 * %s" %변수)
"""

#문제 147
"""
리스트 = [1, 2, 3]
for 변수 in 리스트 :
    result = 3 * int(변수)
    print("3 * %s = %d" %(변수, result))
"""

#문제 148
"""
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[1:]:
  print(변수)
"""

#문제 149
"""
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[::2] :
    print(변수)
"""

#문제 150
"""
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[::-1]:
    print(변수)
"""

#문제 151
"""
리스트 = [3, -20, -3, 44]
for 변수 in 리스트 :
    if 변수 < 0 :
        print(변수)
"""

#문제 152
"""
리스트 = [3, 100, 23, 44]
for 변수 in 리스트 :
    if 변수 % 3 == 0 :
        print(변수)
"""

#문제 153
"""
리스트 = [13, 21, 12, 14, 30, 18]
for 변수 in 리스트 :
    if (변수 < 20) and (변수 % 3 == 0) :
        print(변수)
"""

#문제 154
"""
리스트 = ["I", "study", "python", "language", "!"]
for 변수 in 리스트 :
    if len(변수) >= 3 :
        print(변수)
"""

#문제 155
"""
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트 :
    if 변수.isupper() is True:
        print(변수)
"""

#문제 156
"""
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트 :
    if 변수.isupper() is False:
        print(변수)
"""

#문제 157
"""
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트 :
    print(변수.capitalize())
"""

#문제 158
"""
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for 변수 in 리스트 :
    first, second = 변수.split(".")
    print(first)
"""

#문제 159
"""
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트 :
    first, second = 변수.split(".")
    if second == "h" :
        print(변수)
"""

#문제 160
"""
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트 :
    first, second = 변수.split(".")
    if (second == "h") or (second == "c"):
        print(변수)
"""

#문제 161
"""
리스트 = range(100)
for 변수 in 리스트 :
    print(변수)
"""

#문제 162
"""
리스트 = range(2002,2051,4)
for 변수 in 리스트 :
    print(변수)
"""

#문제 163
"""
리스트 = range(1,31)
for 변수 in 리스트 :
    if 변수 % 3 == 0:
        print(변수)
"""
"""
for num in range(3, 31, 3):
    print (num)
"""

#문제 164
"""
리스트 = range(99,-1,-1)
for 변수 in 리스트 :
    print(변수)

for i in range(100):
    print(99 - i)
"""

#문제 165
"""
리스트 = range(11)
for 변수 in 리스트 :
    변수 = 변수/10
    print(변수)
"""

#문제 166
"""
리스트 = range(1,10)
for 변수 in 리스트 :
    print("3 * %d = %d" %(변수,변수*3))
"""

#문제 167
"""
리스트 = range(1,10)
for 변수 in 리스트 :
    나머지 = 변수 % 2
    if 나머지 != 0:
        print("3 * %d = %d" %(변수,변수*3))
"""

#문제 168
"""
total = 0
for 변수 in range(1,11) :
    total += 변수
print("합 :", total)
"""

#문제 169
"""
total = 0
for 변수 in range(1,11,2) :
    total += 변수
print("합 :", total)
"""

#문제 170
"""
total = 1
for 변수 in range(1,11) :
    total = 변수 * total
print("합 :", total)
"""

#문제 171
"""
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])
"""

#문제 172
"""
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i, price_list[i])
"""

"""
price_list = [32100, 32150, 32000, 32500]
for i, data in enumerate(price_list):
    print(i, data)
"""

#문제 173
"""
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(3-i, price_list[i])
"""

#문제 174
"""
price_list = [32100, 32150, 32000, 32500]
for i in range(1,4):
    print(90+10*i, price_list[i])
"""

#문제 175
"""
my_list = ["가", "나", "다", "라"]
for i  in range(3) :
    print(my_list[i], my_list[i+1])
"""

#문제 176
"""
my_list = ["가", "나", "다", "라", "마"]
for i  in range(3) :
    print(my_list[i], my_list[i+1], my_list[i+2])
"""

#문제 177
"""
my_list = ["가", "나", "다", "라"]
for i  in range(3,0,-1) :
    print(my_list[i], my_list[i-1])
"""

#문제 178
"""
my_list = [100, 200, 400, 800]
for i in range(3) :
    print(my_list[i+1] - my_list[i])
"""

#문제 179
"""
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(4) :
    print((my_list[i] + my_list[i+1] +my_list[i+2])/3)
"""

#문제 180
"""
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(5) :
    result = high_prices[i] - low_prices[i]
    volatility.append(result)

print(volatility)
"""

#문제 181
"""
apart = [ ["101호", "102호"], ["201호", "202호"], ["301호", "302호"] ]

print(apart)
"""

#문제 182
"""
stock = [ ["시가", 100, 200, 300], ["종가", 80, 210, 330] ]
print(stock)
"""

#문제 183
"""
stock = {"시가": [100, 200, 300],"종가": [80, 210, 330]}
print(stock)
"""

#문제 184
"""
stock = {"10/10" : [80, 110, 70, 90], "10/11" : [210, 230, 190, 200]}
"""

#문제 185
"""
apart = [ [101, 102], [201, 202], [301, 302] ]
for 층 in apart :
    for 호수 in 층 :
        print(호수, "호")
"""

#문제 186
"""
apart = [ [101, 102], [201, 202], [301, 302] ]
for 층 in apart[::-1] :
    for 호수 in 층 :
        print(호수, "호")
"""

#문제 187
"""
apart = [ [101, 102], [201, 202], [301, 302] ]
for 층 in apart[::-1] :
    for 호수 in 층[::-1] :
        print(호수, "호")
"""

#문제 188
"""
apart = [ [101, 102], [201, 202], [301, 302] ]
for 층 in apart :
    for 호수 in 층 :
        print(호수, "호")
        print("-----")
"""

#문제 189
"""
apart = [ [101, 102], [201, 202], [301, 302] ]
for 층 in apart :
    for 호수 in 층 :
        print(호수, "호")
    print("-----")
"""

#문제 190
"""
apart = [ [101, 102], [201, 202], [301, 302] ]
for 층 in apart :
    for 호수 in 층 :
        print(호수, "호")
print("-----")
"""

#문제 191
"""
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for OHLC in data :
    for results in OHLC :
        print(results * (1+0.014/100))
"""

#문제 192
"""
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for OHLC in data :
    for results in OHLC :
        print(results * (1+0.014/100))
    print("----")
"""

#문제 193
"""
result = []
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for OHLC in data :
    for results in OHLC :
        result.append(results  * (1+0.014/100))
print(result)
"""

#문제 194
"""
result = []
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for OHLC in data :
    result1 =[]
    for result2 in OHLC :
        result1.append(result2 * (1+0.014/100))
    result.append(result1)    
print(result)
"""

#문제 195
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for 변수 in ohlc[1:] :
    print(변수[3])
"""


#문제 196
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for 변수 in ohlc[1:] :
    if 변수[3] > 150 :
        print(변수[3])
"""

#문제 197
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for 변수 in ohlc[1:] :
    if 변수[3] >= 변수[0] :
        print(변수[3])
"""

#문제 198
"""
volatility =[]

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for 변수 in ohlc[1:] :
    volatility.append(변수[1]-변수[2])
print(volatility)
"""

#문제 199
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for 변수 in ohlc[1:] :
    if 변수[3] > 변수[0] :
        print(변수[1]-변수[2])
"""

#문제 200
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
total = 0
for 변수 in ohlc[1:] :
    total += (변수[3]-변수[0])
print(total)
"""

#문제 201
"""
def print_coin():
    print("비트코인")
"""

#문제 202
"""
def print_coin():
    print("비트코인")

print_coin()    
"""

#문제 203
"""
def print_coin():
    print("비트코인")

for i in range(100):
    print_coin()
"""

#문제 204
"""
def print_coins():
    for i in range(100):
        print("비트코인")

print_coins()
"""

#문제 205
"""
hello()
def hello():
    print("Hi") #hello함수가 정의되기 전에 호출했기 때문에
"""

#문제 206
"""
def message() :
    print("A")
    print("B")

message()       # message함수 출력 
print("C")      # c 출력
message()       # message함수 출력
"""

#문제 207
"""
print("A")      # A 출력

def message() :
    print("B")  # message함수 정의

print("C")      # C 출력
message()       # B 출력
"""

#문제 208
"""
print("A")          # A 출력
def message1() :
    print("B")      # message1 정의
print("C")          # C 출력
def message2() :
    print("D")      # message2 정의
message1()          # B 출력
print("E")          # E 출력
message2()          # D 출력
"""

#문제 209
"""
def message1():     
    print("A")      # message1 정의

def message2():     
    print("B")      
    message1()      # message2 정의(B 다음 A 출력)

message2()          # B 다음 A 출력
"""

#문제 210
"""
def message1():
    print("A")              # message1 정의

def message2():
    print("B")              # message2 정의

def message3():
    for i in range (3) :
        message2()
        print("C")          
    message1()              # message3 정의((B,C 3번 반복 + A)출력 )

message3()                  # BCBCBCA 출력
"""

#문제 211
"""
def 함수(문자열) :
    print(문자열)

함수("안녕")            # 문자열 = 안녕
함수("Hi")              # 문자열 = Hi
"""

#문제 212
"""
def 함수(a, b) :
    print(a + b)

함수(3, 4)              # 3 + 4
함수(7, 8)              # 7 + 8
"""

#문제 213
"""
def 함수(문자열) :
    print(문자열)

함수()                  #문자를 넣어줘야 출력
"""

#문제 214
"""
def 함수(a, b) :
    print(a + b)

함수("안녕", 3)         # 안녕이 아니라 숫자가 들어가야 된다.
"""

#문제 215
"""
def print_with_smile (string) :
    print (string + ":D")

print_with_smile("반갑습니다")
"""

#문제 216
"""
def print_with_smile (string) :
    print (string + ":D")

print_with_smile("안녕하세요")
"""

#문제 217
"""
def print_upper_price(price) :
    print(price * 1.3)
"""

#문제 218
"""
def print_sum (a, b) :
    print (a + b)
"""

#문제 219
"""
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)

print_arithmetic_operation(3, 4)
"""

#문제 220

"""
def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)

print_max(1, 2, 3)
"""

#문제 221
"""
def print_reverse(string) :
    print(string[::-1])

print_reverse("python")
"""

#문제 222
"""
def print_score(score_list) :
    print(sum(score_list)/len(score_list))

print_score ([1, 2, 3])
"""

#문제 223
"""
def print_even (my_list) :
    for v in my_list :
        if v % 2 == 0 :
            print(v)
"""

#문제 224
"""
def print_keys(dic):
    for keys in dic.keys():
        print(keys)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})
"""

#문제 225
"""
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key (dic, key) :
    print(my_dict[key])

print_value_by_key (my_dict, "10/26")
"""

#문제 226 - 이해 필요
"""
def print_5xn(string):
    chunk_num = int(len(string) / 5)
    for i in range(chunk_num + 1) :
        print(string[i * 5: i * 5 + 5])

print_5xn("아이엠어보이유알어걸")
"""

#문제 227
"""
def print_mxn(string, num):
    chunk_num = int(len(string) / num)
    for i in range(chunk_num + 1) :
        print(string[i * num: i * num + num])

print_mxn("아이엠어보이유알어걸", 3)
"""

#문제 228
"""
def calc_monthly_salary(annual_pay) :
    monthly_pay = int(annual_pay / 12)
    return monthly_pay

print(calc_monthly_salary(12000000))
"""

#문제 229
"""
def my_print (a, b) :
    print("왼쪽 :", a)       
    print("오른쪽 :", b)

my_print(a=100, b=200)          # 왼쪽 : a , 오른쪽 : b
"""

#문제 230
"""
def my_print (a, b) :
    print("왼쪽 :", a)
    print("오른쪽 :", b)        # 왼쪽 : a , 오른쪽 : b

my_print(b=100, a=200)
"""

#문제 231
"""
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print (result)             #정의된 함수 안의 변수는 출력 X
"""

#문제 232
"""
def make_url(string) :
    return "www." + string + ".com"

print(make_url("naver"))
"""

#문제 233
"""
def make_list(string) :
    list = []
    string1 = len(string)
    for i in range(string1) :
        list.append(string[i])
    return list    

print(make_list("abcd"))
"""

#문제 234
"""
def pickup_even(items):
    result = []
    for item in items:
        if item % 2 == 0:
            result.append(item)
    return result
"""

#문제 235
"""
def convert_int (string) :
    return int(string.replace(",", ""))

print(convert_int("1,234,567"))
"""

#문제 236
"""
def 함수(num) :
    return num + 4

a = 함수(10)            # a = 14
b = 함수(a)             # b = 18
c = 함수(b)             # c = 22
print(c)
"""

#문제 237
"""
def 함수(num) :             
    return num + 4          

c = 함수(함수(함수(10)))        # c = 10 + 4 + 4 + 4
print(c)
"""

#문제 238
"""
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)           # a = 14
c = 함수2(a)            # c = 140
print(c)
"""

#문제 239
"""
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)           # c = 함수1(12) = 12 + 4 = 16
print(c)
"""

#문제 240
"""
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)                    #c = 함수2(2) = 함수1(12) = 함수0(14) = 28
print(c)
"""