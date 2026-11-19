#1 출력 시 " , ' 구분하여 출력하기
print('신씨가 소리질렀다. "도둑이야".')

#2
print("Mary's cosmetics")

#3 print(sep =' ')
print(1,2,3,4,5,6, sep ='/')

#python 300제 007번 문제
print("naver", "kakao" , "sk", "samsung")
#naver;kakao;sk;samsung
print("naver", "kakao", "samsung", sep=";")


'''for i in range(7):
    print(i)'''

print("first", end=""); print("second")

#13번

s = "hello"
t = "python"
print(s+"!", t)

#type 값의 타입을 알려주는 함수
a=128
print(type(a)) #int 정수

a= "128"
print(type(a)) #str 문자열

a= 12.5
print(type(a)) #float 실수


#문자(열) -> 정수 (str -> int)
a = "128"
b = int(a)
print(type(a))
#대입 해서 변수를 int 변경
a =int(a)

#정수 -> 실수
b= 123
b= float(b)

#정수 -> 문자열
c = 123
c= str(c)


#문자열 인덱싱 ->p t
letters = 'python'
print(letters[0], letters[2])

#문자열 슬라이싱 -> 뒤에 4자리
license_plate = "24가 2210"
print(license_plate[-4::])

#문자열 슬라이싱 step
string = "홀짝홀짝홀짝"
print(string[::2]) #홀홀홀
print(string[1::2]) #짝짝짝


#문자열 슬라이싱 거꾸로 출력
srting = "PYTHON"
print(string[::=1])

#문자열 치환(replace)
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
#phone_number = phone_number.replace("-", " ")
#print(phone_number)

#python 300제 026
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace('-', '')
print(phone_number1)

#python 300제 027
url = "http://sharebook.kr"   #kr
url = url.split(".")
print(url[-1])

#문자 + 문자 (더하기 연산 -> 연결)
a= "3"
b= "4"
print(a+b) #"34"

#문자 * 숫자 (곱하기 -> 문자를 숫자만큼 반복해서 출력)
a= "hi"
print(a*10) #"hihihihihihihihihihi"

# python 300제 034
t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

# python 300제 035 ~ 037 검토

# python 300제 038

상장주식수 = "5,969,782,550"
상장주식수= int(상장주식수.replace("."," "))

#040 strip() 좌우 공백을 제거
data = "    삼성전자       "  
print(data.strip())


# 049 date  ="2020-05-01" -> 연도, 월, 일
date = "2020-05-01"
temp = date.split("-")
year = temp [0]
month = temp [1]
day = temp[2]

print(year)
print(month)
print(day)
print(temp)

#051 리스트 생성
movies = ["닥터 스트레인지", "스플릿", "럭키"]

# 052 리스트에 원소 추가 -> append("값") (맨 뒤에 값을 추가)
movies.append("배트맨")
print(movies)

# 053 리스트에 원소 추가 (특정위치) -> (인덱스 , 값)
movie.insert(1, "슈퍼맨")
print(movie)


# 054 리스트에 원소 삭제 (remove("값"), del 리스트이름.[인덱스])
# pop(인덱스)
movies.remove("럭키")
print("remove:", movies)
movies.append("럭키")
del movies[4]
print("del: ", movies)


# 056 리스트에 랍 (더하기 연산) 중복허용
a = ['a', 'b', 'c']
b = ['a', 'b', 'c']
c = a+b
print(c)

# 057 리스트값 중에 최대값 (max()) , 최소값 (min())
a_list = [1,2,3,4,5,6,7,8]
print(max(a_list))
print(min(a_list))

# 058 리스트 요소값에 합 (sum())
print(sum(a_list))

# 059 리스트 요소에 개수 (len())
print(len(a_list))

#060 리스트 요소값에 평균 (sum()/len())
print(sum(a_list)/len(a_list))

