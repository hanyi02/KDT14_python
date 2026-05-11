#  Series, DataFrame 연산 과제
# 이한이
"""
【사용 데이터 1 】 --------------------------------------------------------------------- 
다음 조건에 맞게 midterm Series와 final Series를 생성하세요. 
midterm : 중간고사 점수를 저장합니다. 
인덱스 값 
김민수 80 
이서연 90 
박지훈 75 
최유진 88 

final : 기말고사 점수를 저장합니다. 
인덱스 값 
김민수 85 
이서연 92 
박지훈 78 
최유진 95 
조건: midterm과 final은 모두 학생 이름을 인덱스로 갖는 Series로 생성하세요. 
-------------------------------------------------------------------------------------- 
"""
import pandas as pd

Mid= pd.Series([80, 90, 75, 88], index=['김민수', '이서연', '박지훈', '최유진'])
Final= pd.Series([85, 92, 78, 95], index=['김민수', '이서연', '박지훈', '최유진'])


# 문제 01) midterm과 final을 더하여 학생별 총점을 출력하세요. 

print(f"총점 ---------------\n{Mid+Final}")

# 문제 02) final에서 midterm을 빼서 기말고사 점수 변화량을 출력하세요. 
print(f"점수 변화량 ---------------\n{Final-Mid}")

# 문제 03) midterm과 final을 이용하여 학생별 평균 점수를 출력하세요. 
print(f"평균 점수 ---------------\n{(Final+Mid)/2}")

# 문제 04) midterm의 모든 점수에 5점을 더한 결과를 출력하세요. 
print(f"5점을 더한 결과 ---------------\n{Mid+5}")

# 문제 05) final 점수가 90점 이상인 학생을 True/False로 출력하세요.
print(f"90점 이상인 학생 ---------------\n{Final>=90}")

# 문제 06) final 점수가 90점 이상인 학생의 점수만 출력하세요.
print(f"90점 이상인 학생 점수 ---------------\n{Final[Final>= 90]}")

# 【사용 데이터 2 】 --------------------------------------------------------------------- 
# 다음 조건에 맞게 class_a DataFrame과 class_b DataFrame을 생성하세요. 
# class_a : 아래 학생별 과목 점수를 저장합니다. 
# 이름 국어 영어 수학 
# 김민수 80 85 90 
# 이서연 90 88 95 
# 박지훈 75 79 70 

# 조건: 학생 이름을 인덱스로 갖는 DataFrame으로 생성하세요. 
# class_b : 아래 학생별 과목 점수를 저장합니다. 
# 이름 국어 영어 수학 
# 최유진 88 90 93 
# 정하늘 76 82 80 
# 한지민 92 85 96 
# 조건: 학생 이름을 인덱스로 갖는 DataFrame으로 생성하세요. 
# -------------------------------------------------------------------------------------- 

class_a= pd.DataFrame(
    {
        "국어": [80, 90, 75],
        "영어": [85, 88, 79],
        "수학": [90, 95, 70]
    },
    index=["김민수", "이서연", "박지훈"]
)

class_b= pd.DataFrame(
    {
        "국어": [88, 76, 92],
        "영어": [90, 82, 85],
        "수학": [93, 80, 96]
    },
    index=["최유진", "정하늘", "한지민"]
)


# 문제 07) class_a DataFrame의 모든 점수에 10점을 더한 결과를 출력하세요. 
print(f"점수+ 10 ---------------\n{class_a+10}")

# 문제 08) class_a DataFrame에 총점 열을 추가하세요.
#  총점은 국어 + 영어 + 수학으로 계산합니다. 
class_a["총점"] = class_a["국어"] + class_a["영어"] + class_a["수학"]
print(f"총점 ---------------\n{class_a}")


# 문제 09) class_a DataFrame에 평균 열을 추가하세요.
#  평균은 총점 / 3으로 계산합니다. 
class_a["평균"] = class_a["총점"] / 3
print(f"총점 ---------------\n{class_a}")


# 문제 10) class_a DataFrame에서 각 점수가 80점 이상인지 True/False로 출력하세요. 
print(f"80점 이상 ---------------\n{class_a[['국어', '영어', '수학']] >= 80}")

# 문제 11) class_a DataFrame에서 수학 점수가 80점 이상인 학생만 출력하세요 
print(f"수학 80점 이상 ---------------\n{class_a[['수학']] >= 80}")


# 문제 12) class_a와 class_b를 행 방향으로 연결하여 all_students DataFrame을 생성하세요.
all_students = pd.concat([class_a[["국어", "영어", "수학"]], class_b], axis=0)
print(f"all_students ---------------\n{all_students}")


# 문제 13) all_students DataFrame에 총점과 평균 열을 추가하세요. 
all_students["총점"] = all_students["국어"] + all_students["영어"] + all_students["수학"]
all_students["평균"] = all_students["총점"] / 3
print(f"all_students ---------------\n{all_students}")

# 문제 14) 다음 두 Series를 생성한 후 더하세요. 
# 조건 
# - s1과 s2는 모두 문자열 인덱스를 갖는 Series로 생성하세요. 
# - s1 Series의 인덱스는 A, B, C 이고 데이터는 10, 20, 30 
# - s2 Seires의 인덱스는 B, C, D 이고 데이터는 1, 2, 3  
s1 = pd.Series([10, 20, 30], index=["A", "B", "C"])
s2 = pd.Series([1, 2, 3], index=["B", "C", "D"])
print(f"s1 + s2 ---------------\n{s1 + s2}")



# 문제 15) 다음 조건을 모두 수행하세요. 
# → midterm과 final을 이용하여 exam DataFrame을 생성하세요. 
# → exam DataFrame의 컬럼명은 중간, 기말로 지정하세요. 
# → 총점 열을 추가하세요. 
# → 평균 열을 추가하세요. 
# → 기말 점수가 90점 이상인 학생만 출력하세요. 
# → 평균 점수가 높은 순서대로 정렬하세요.

exam = pd.DataFrame({
    "중간": Mid,
    "기말": Final
})

exam["총점"] = exam["중간"] + exam["기말"]
exam["평균"] = exam["총점"] / 2

print(f"exam DataFrame ---------------\n{exam}")
print(f"기말 점수 90점 이상 ---------------\n{exam[exam['기말'] >= 90]}")
print(f"평균 점수 높은 순 정렬 ---------------\n{exam.sort_values('평균', ascending=False)}")


