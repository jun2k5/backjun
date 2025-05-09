# 1152문제
# 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

# 입력
# 첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.

# 출력
# 첫째 줄에 단어의 개수를 출력한다.


def solution(S:str):
    w = list(S.split())

    print(len(w))

 

if __name__ == "__main__":
    S = input()

    solution(S)


"""
-Learning Point
리스트 함수들
append(a) 배열 마지막에 a원소 추가
clear() 배열 초기화
copy() 배열 복사
count(a) a원소의 개수
extend(b) b배열과 결합 
index(a) a원소의 위치 (메모리 주소 아님)
insert(a, b) a위치에 b삽입
pop(a) a원소 POP
remove(a) a원소 삭제
reverse() 배열 역순
sort() 배열 정렬 역순가능

"""
