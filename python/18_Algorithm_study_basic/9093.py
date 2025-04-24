# 단어 뒤집기 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	44575	24114	18261	54.985%
# 문제
# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 문장이 하나 주어진다. 단어의 길이는 최대 20, 문장의 길이는 최대 1000이다. 단어와 단어 사이에는 공백이 하나 있다.

# 출력
# 각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.


def solution(N:int, data:list):
    temp = []                           # 단어 배열 선언

    for i in range(N):

        for j in range(len(data[i])):
            
            if data[i][j] == ' ':       #단어의 공백문자를 만났을 때
                temp.reverse()          #단어 뒤집기
                for k in temp:          #출력
                    print(k, end='')
                print(end = ' ')
                temp.clear()            #단어 배열 비우기
                continue
            
            temp.append(data[i][j])

            if j == len(data[i])-1:     #문장의 끝에 도달했을 때
                temp.reverse()
                for k in temp:
                    print(k, end='')
                print(end = ' ')
                temp.clear()
                break
            
        print()

        


if __name__ == "__main__":
    N = int(input())                    #문장 개수 입력
    data = []

    for i in range(N):                  # 문장 입력
        data.append(list(input()))
    
    solution(N, data)

#    print(data)





################### 다른 사람의 풀이 
# import sys
# N = int(input())

# for _ in range(N):
#     str = sys.stdin.readline().rstrip()
#     words = list(str.split())
#     reverse_words = []

#     for word in words:
#         reverse_words.append(word[::-1])

#     answer = " ".join(reverse_words)
#     print(answe


