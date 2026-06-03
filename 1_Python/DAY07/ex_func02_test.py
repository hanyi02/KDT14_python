## =================================================
## 사용자 정의 함수 실습
## =================================================
## [1] 사용자가 지정한 범위의 숫자들 중에서 짝수인 숫자만
##     합계를 해서 반환해주는 함수
## 예시 : 5, 100 ==> 범위에서 2의 배수만 합계 계산
## =================================================
## -------------------------------------------------
## 함수이름 : getEvenNums
## 함수기능 : 범위내의 짝수 데이터의 합계 계산 후 반환
## 매개변수 : start, stop
## 함수결과 : total
## -------------------------------------------------
def getEvenNums(start, stop):
    total = 0
    for num in range(start, stop+1):
        if num%2 == 0: 
            total += num 
    return total

def getEvenNums(start, stop):
    total = [ num for num in range(start, stop+1) if not num%2 ]
    return sum(total)

## =================================================
## [2] 전달받은 단어에 대한 기계코드값 출력해주는 함수
## 예시 : 'Hello' => 모니터에 'Hello' 기계코드 : 11------00010
## =================================================
## -------------------------------------------------
## 함수이름 : convertCode
## 함수기능 : 단어에 대한 기계코드값 출력해주는 함수
## 매개변수 : word
## 함수결과 : X
## -------------------------------------------------
def convertCode(word):
    code =""
    for w in word:
        code = code +" " + bin(ord(w))[2:]
    print(f"{word}기계코드 : { code }")


def convertCode2(word):
    code = [ bin(ord(w))[2:] for w in word ] 
    code = " ".join(code)
    print(f"{word}기계코드 : { code }")


## 함수 호출 ------------------------------------------
convertCode2("Apple")
convertCode2("Korea")

print(f"5 ~ 10 : {getEvenNums(5, 10)}")
print(f"1 ~ 10 : {getEvenNums(1, 10)}")