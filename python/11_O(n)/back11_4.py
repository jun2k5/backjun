# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	512 MB	31703	16141	15105	51.247%
# 문제
# 오늘도 서준이는 알고리즘의 수행시간 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# 입력의 크기 n이 주어지면 MenOfPassion 알고리즘 수행 시간을 예제 출력과 같은 방식으로 출력해보자.

# MenOfPassion 알고리즘은 다음과 같다.

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
# 입력
# 첫째 줄에 입력의 크기 n(1 ≤ n ≤ 500,000)이 주어진다.

# 출력
# 첫째 줄에 코드1 의 수행 횟수를 출력한다.

# 둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

def MenOfPassion(A:list, n:int):
    sum = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            sum = sum + A[i] * A[j] # 코드1
                #시간 복잡도 : (n**2)
                #최고 차항의 계수 : 2
    return sum

if __name__ == "__main__":
    n = int(input())
    print(int(n*(n-1)/2))
    print(2)
