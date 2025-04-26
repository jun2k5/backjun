# 단어 뒤집기 2
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	512 MB	38603	21812	16931	56.953%
# 문제
# 문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.

# 먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.

# 알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
# 문자열의 시작과 끝은 공백이 아니다.
# '<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
# 태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고, '<'와 '>' 사이에는 알파벳 소문자와 공백만 있다. 단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다. 태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

# 입력
# 첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하이다.

# 출력
# 첫째 줄에 문자열 S의 단어를 뒤집어서 출력한다.

import sys
input = sys.stdin.readline


def solution(data:list):

    temp = []                           # 단어 배열 선언

    for i in range(len(data)):

        if data[i] == '<':
            temp.reverse()          #태그 전 단어 뒤집기
            for k in temp:          #출력
                print(k, end='')
            temp.clear()            #단어 배열 비우기


        if data[i] == ' ' and not "<" in temp:       #태그 포함이 안된 단어의 공백문자를 만났을 때
            temp.reverse()          #단어 뒤집기
            for k in temp:          #출력
                print(k, end='')
            print(end = ' ')
            temp.clear()            #단어 배열 비우기
            continue
        
        temp.append(data[i])

        if data[i] == '>':          #태그 종료문자를 만났을 때
            for k in temp:          #출력
                print(k, end='')
            temp.clear()            #단어 배열 비우기            

        if i == len(data)-1:     #문장의 끝에 도달했을 때
            temp.reverse()
            for k in temp:
                print(k, end='')
            print(end = ' ')
            temp.clear()
            break

        


if __name__ == "__main__":
    data = list(input().rstrip())
    
    solution(data)
