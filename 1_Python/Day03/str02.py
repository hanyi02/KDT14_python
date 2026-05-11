## =======================================
## [4] 원소/ 요소 변경 후 반환=> replace(문자/ 문자열)
## * 변환된 새로운 str 반환
## => 원문에 적용 안 됨
## =======================================
## "good luck"---> 'Good Luck
msg="good luck"

# msg[0]="G"
# print(f"msg=> {msg}") # not support -> 인덱스 기반 원소값 변경 미지원=> 메서드 제공

## replace(이전문자/문자열, 새로운문자/ 문자열) 메서드
new_msg=msg.replace("g", "G")
# print(f"msg=> {msg}")
print(f"msg=> {new_msg}") 

msg="good luck good luck good luck good luck good luck"
new_msg=msg.replace("g", "G", 2) # 지정된 개수만큼
print(new_msg)


## =======================================
## [5] 1개의 str=> 여러개 str분리: split()메서드
## * [기본] 공백문자 기준으로 분리
## * 메서드 사용 시 분리 기준 문자/ 문자열 설정 가능
## * 리스트에 여러개 분리된 str 담아서 반환
## =======================================

data= "Happy New Year 2026!!"

ret= data.split()
print(f"data {data}, {type(data)}, {len(data)}개")
print(f"ret {ret}, {type(ret)}, {len(ret)}개")

data= "Happy New Year 2026!!"
ret= data.split("-")
print(f"data {data}, {type(data)}, {len(data)}개")
print(f"ret {ret}, {type(ret)}, {len(ret)}개")


## =======================================
## [6] 여러개 str => 1개 str 연결: join() 메서드
## * [설정] 연결문자 지정

## =======================================


#여러개 str 분리
ret= data.split()
#1개 str 연결
new_ret="-".join(ret)

print(ret, new_ret, sep= '==>')