# 단어 정렬
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	225072	95872	71665	40.810%
# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다.

import sys
input = sys.stdin.readline

def solution(data:list):
    
    data.sort()
    data.sort(key = len)
  
    for i in data:
        print(i)
# import sys하면 엔터가 한번 더 쳐진다 왜?

# 이유
# sys.stdin.readline는 엔터까지 입력되기 때문

# 입력받은 data 리스트트
# ['but\n', 'i\n', 'wont\n', 'hesitate\n',
# 'no\n', 'more\n', 'no\n', 'more\n', 'it\n', 'cannot\n', 'wait\n', 'im\n', 'yours\n']



if __name__ == "__main__":
    N = int(input())
    data = []

    for i in range(N):
        data.append(input().strip())
            # sys.stdin.realine 사용 시 input().strip()을 사용하여 개행문자를 처리할 수 있다.

#    print(data)

    data = set(data)

    solution(list(data))




