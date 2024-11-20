# 2444문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

def solution(N:int):
    #\n For문
    for i in range(0, 2*N - 1):
        if i < N:
        #공백 For문
            for k in range(0, N-i - 1):
                print(" ", end='')
        #star For문
            for j in range(0, 1 + 2*i):
                print("*", end='')
        else:
        #공백 For문
            for k in range(0, i-N+1):
                print(" ", end='')
        #star For문
            for j in range(0, 2*(2*N - i) - 3):
                print("*", end='')
        print()

          
# N : 5     2*N:10

# looq:     1 2 3 4 5        6 7 8 9
# i :       0 1 2 3 4        5 6 7 8
# i - N + 1 :                1 2 3 4
# \n :      1 1 1 1 1        1 1 1 1
# space :   5 4 3 2 1        2 3 4 5 
# star :    1 3 5 7 9        7 5 3 1
#                            3 5 7 9

if __name__ == "__main__":
    N = int(input())

    solution(N)

