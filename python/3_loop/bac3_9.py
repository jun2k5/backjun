# 2439문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

def solution():
    #N 입력
    N = int(input())
    
    #N번 개행문자 For문
    for i in range(0, N):
        #N - (i+1) <- N에서 별갯수를 뺀만큼 공백문자
        for j in range(0, N-(i+1)):
            print(" ", end="")
        #i+1만큼(0에서 시작하기 때문에 i + 1개) 별출력
        for k in range(0, i+1):
            print("*", end="")
        print()


if __name__ == "__main__":
    solution()


"""
-Learning Point
하나하나 규칙을 잘 살펴볼것.

"""