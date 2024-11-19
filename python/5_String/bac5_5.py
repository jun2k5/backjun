# 11720문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.

def solution(N:int):
    result = 0
    
    S = input()

    for i in range(0, N):
    #입력값 중에 숫자가 아닌 경우 종료
        try:
            result += int(S[i])

        except:
            print("오류")
            break

    print(result)



if __name__ == "__main__":

    while True:
        try:
            N = int(input())
            break
        except:
            print("오류")
            print("다시입력")

    solution(N)

"""
-Learning Point
사용자 입장에서 입력값이 엉망진창인 경우도 생각해보면
코드를 좀 더 잘 작성할 수 있을것이다.
"""

