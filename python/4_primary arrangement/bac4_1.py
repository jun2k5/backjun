# 10807문제
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

# 출력
# 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
import sys

def solution():
    #N 입력
    N = int(sys.stdin.readline())
    #N개의 일차 배열 선언
    A = []
    #cnt = 같은 숫자개수, 0으로 초기화
    cnt = 0

    #A 배열 값 입력
    A = list(map(int, sys.stdin.readline().split()))

#   print(len(A))
#    print(type(A[0]))

    B = int(sys.stdin.readline())
#    print(type(B))

    for i in range(0, len(A)):
        if int(A[i]) == B:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    solution()


"""
-Learning Point
map()함수로 연속된 입력값을 리스트로 받기 위해서는 리스트형으로 형변환해야한다.
map()함수는 map객체를 반환한다
arr = list(map(int, input().split()))

리스트의 길이는 len()함수로 알 수 있다.


### 정수 1개 입력받기
N = int(input())
 
### 한줄 정수 리스트 입력받기
li = [*map(int,input().split())]
 
### 여러개 정수 입력받기
a,b,c = map(int,input().split())
 
### 여러 줄의 정수 리스트 입력받기
n = int(input())
li = [int(input()) for _ in range(n)]
## n 없이 한 줄로
li = [int(input()) for _ in range(int(input()))]
 
### N행 배열 입력받기
#### 숫자인 경우
N=int(input()) # N개의 행
arr=[[*map(int,input().split())] for _ in range(N)]
 
#### 문자열인 경우
N=int(input()) # N개의 행
arr=[list(input()) for _ in range(N)]
 
## 입력 빠르게하기
import sys
input=sys.stdin.readline # input함수 바꾸기
"""