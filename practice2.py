# 문제 241
"""
import datetime

now = datetime.datetime.now()
print(now)
"""

#문제 242
"""
import datetime

now = datetime.datetime.now()
print(type(now))
"""

#문제 243
"""
import datetime

now = datetime.datetime.now()

for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)
"""

#문제 244
"""
import datetime

now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))
"""

#문제 245
"""
import datetime

day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))
"""

#문제 246
"""
import time
import datetime

while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)
"""

#문제 247


#문제 248
"""
import os
ret = os.getcwd()
print(ret, type(ret))
"""


#문제 249
"""
import os
os.rename("C:/Users/User/Desktop/before.txt", "C:/Users/User/Desktop/python 강좌.txt")
"""

#문제 250
"""
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)
"""

#문제 251


#문제 252
"""
class Human:
    pass
"""

#문제 253
"""
class Human:
    pass

areum = Human()
"""

#문제 254
"""
class Human:
    def __init__(self):
        print("응애응애")

areum = Human()
"""

#문제 255
"""
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
print(areum.name)
"""

#문제 256
"""
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("조아름", 25, "여자")
print(areum.name)
print(areum.age)
print(areum.sex)
"""

#문제 257
"""
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: %s 나이: %d 성별: %s" %(self.name, self.age, self.sex))

areum = Human("아름", 25, "여자")
areum.who()
"""

#문제 258 - % 쓰면 안됨. 미상은 'String' 타입이기 때문에
"""
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
     print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        
areum = Human("불명", "미상", "모름")
areum.who()    

areum.setInfo("아름", 25, "여자")
areum.who()    
"""

#문제 259
"""
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
del(areum)
"""

#문제 260
"""
class OMG : 
    def print() :
        print("Oh my god")

myStock = OMG()
myStock.print()
"""

#문제 261
"""
class Stock:
    pass
"""

#문제 262
"""
class Stock:
    def __init__(self,name,num):
        self.name = name
        self.num = num

삼성 = Stock("삼성전자", "005930")

print("{}, {}" .format(삼성.name, 삼성.num))
"""

#문제 263
"""
class Stock:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def set_name(self, name):
        self.name = name

a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)
"""

#문제 264
"""
class Stock:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def set_name(self, name):
        self.name = name

a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)
"""

#문제 265
"""
class Stock:
    def __init__(self, name, num):
        self.name = name
        self.code = num

    def set_name(self, name):
        self.name = name
    
    def set_code(self, num):
        self.code = num
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)
print(삼성.get_name())
print(삼성.get_code())
"""

#문제 266
"""
class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name
    
    def set_code(self, code):
        self.code = code
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
"""

#문제 267
"""
class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name
    
    def set_code(self, code):
        self.code = code
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(삼성.name, 삼성.code, 삼성.per, 삼성.pbr, 삼성.배당수익률)
"""

#문제 268
"""
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend
"""


#문제 269
"""
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
삼성.set_per(12.75)
print(삼성.per)
"""

#문제 270
"""
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)


for i in 종목:
    print(i.code, i.per)
"""

#문제 271
"""
import random

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      
        num2 = str(num2).zfill(2)      
        num3 = str(num3).zfill(6)  
        self.account_number = num1 + '-' + num2 + '-' + num3

kim = Account("김민수", 100)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account_number)
"""

#문제 272
"""
import random

class Account:
    
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      
        num2 = str(num2).zfill(2)      
        num3 = str(num3).zfill(6)      
        self.account_number = num1 + '-' + num2 + '-' + num3  

        Account.account_count += 1


kim = Account("김민수", 100)
lee = Account("이민수", 100)
Park = Account("박민수", 100)
print(Account.account_count)
"""

#문제 273
"""
import random

class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      
        num2 = str(num2).zfill(2)      
        num3 = str(num3).zfill(6)      
        self.account_number = num1 + '-' + num2 + '-' + num3 
        Account.account_count +=1

    @classmethod   
    def get_account_num(cls):
        print(cls.account_count)


kim = Account("김민수", 100)
lee = Account("이민수", 100)
kim.get_account_num()
"""

#문제 274 - cls는 clas에서 가져오는 거라 그런듯? / 
"""
import random

class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      
        num2 = str(num2).zfill(2)      
        num3 = str(num3).zfill(6)      
        self.account_number = num1 + '-' + num2 + '-' + num3  
        Account.account_count +=1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
"""

#문제 275
"""
import random


class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  
        num2 = str(num2).zfill(2) 
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3 
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

k = Account("kim", 100)
k.deposit(100)
k.withdraw(90)
print(k.balance)
k.withdraw(50)
print(k.balance)
k.withdraw(70)          #잔고 이상으로 출력하려 했기 때문에 출력 X
print(k.balance)
"""

#문제 276
"""
import random


class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  
        num2 = str(num2).zfill(2)  
        num3 = str(num3).zfill(6)  
        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)


p = Account("파이썬", 10000)
p.display_info()
"""

#문제 277
"""
import random


class Account:
    
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

 
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  
        num2 = str(num2).zfill(2)  
        num3 = str(num3).zfill(6)  
        self.account_number = num1 + '-' + num2 + '-' + num3  
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
            
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

p = Account("파이썬", 10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.balance)
"""

#문제 278
"""
import random


class Account:
    
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

 
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  
        num2 = str(num2).zfill(2)  
        num3 = str(num3).zfill(6)  
        self.account_number = num1 + '-' + num2 + '-' + num3  
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
            
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

data = []
k = Account("KIM", 10000000)
l = Account("LEE", 10000)
p = Account("PARK", 10000)

data.append(k)
data.append(l)
data.append(p)

print(data)
"""

#문제 279
"""
import random


class Account:
    
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

 
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  
        num2 = str(num2).zfill(2)  
        num3 = str(num3).zfill(6)  
        self.account_number = num1 + '-' + num2 + '-' + num3  
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
            
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

data = []
k = Account("KIM", 10000000)
l = Account("LEE", 10000)
p = Account("PARK", 10000)
data.append(k)
data.append(l)
data.append(p)

for c in data:
    if c.balance >= 1000000:
        c.display_info()
"""

#문제 280

"""
import random


class Account:
    
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

 
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  
        num2 = str(num2).zfill(2)  
        num3 = str(num3).zfill(6)  
        self.account_number = num1 + '-' + num2 + '-' + num3  
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  

    def deposit(self, amount):
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
            
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)


k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()
"""

#문제 281
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

car = 차(2,100)
print(car.바퀴)
print(car.가격)
"""

#문제 282
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자전차(차):
    pass
"""

#문제 283
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자전차(차):
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

bicycle = 자전차(2, 100)
print(bicycle.가격)
"""

#문제 284
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

bicycle = 자전차(2, 100, "시마노")
print(bicycle.구동계)
"""

#문제 285
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)


car = 자동차(4, 1000)
car.정보()      
"""

#문제 286
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)
        

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()
"""

#문제 287
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)
        print("구동계 ", self.구동계)

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()
"""

#문제 288
"""
class 부모:
    def 호출(self):
        print("부모호출")

class 자식(부모):
    def 호출(self):
        print("자식호출")


나 = 자식()
나.호출()
"""

#문제 289
"""
class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")

나 = 자식()
"""

#문제 290
"""
class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()

나 = 자식()
"""