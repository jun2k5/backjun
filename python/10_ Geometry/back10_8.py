# 세 막대
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	27371	18506	17193	68.270%
# 문제
# 영선이는 길이가 a, b, c인 세 막대를 가지고 있고, 각 막대의 길이를 마음대로 줄일 수 있다.

# 영선이는 세 막대를 이용해서 아래 조건을 만족하는 삼각형을 만들려고 한다.

# 각 막대의 길이는 양의 정수이다
# 세 막대를 이용해서 넓이가 양수인 삼각형을 만들 수 있어야 한다.
# 삼각형의 둘레를 최대로 해야 한다.
# a, b, c가 주어졌을 때, 만들 수 있는 가장 큰 둘레를 구하는 프로그램을 작성하시오. 

# 입력
# 첫째 줄에 a, b, c (1 ≤ a, b, c ≤ 100)가 주어진다.

# 출력
# 첫째 줄에 만들 수 있는 가장 큰 삼각형의 둘레를 출력한다.

def solution(a:int, b:int, c:int) -> None:
    list = sorted([a,b,c])
    result = sum(list)
    if list[0] + list[1] <= list[2] :
        result = (list[0] + list[1])*2 - 1

    print(result)

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    solution(a, b, c)


