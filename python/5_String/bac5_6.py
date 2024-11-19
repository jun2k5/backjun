# 10809문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

#알파벳 모음과 입력값을 받아 알파벳의 위치를 알려주는 배열 출력
def solution(apb:list, S:str):
    #알파벳 위치 배열 생성, 초기값 -1
    result = [-1] * 26

    #입력값의 알파벳이 어디있는지 탐색 For문
    for i in range(0, len(apb)):
        for j in range(0, len(S)):
            if apb[i] in S[j] and result[i] == -1:
                result[i] = j
    #출력
    for i in result:
        print(i, end=" ")

if __name__ == "__main__":
    #문제 입력
    S = input()

    #알파벳 배열 생성
    #아스키코드 활용하여 초기값 설정 For문
    apb = [] * 26   
    for i in range(0,26):
        apb.append(chr(97 + i))

    solution(apb, S)


    

