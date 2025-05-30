# 로프 실패
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	192 MB	76091	34319	27410	43.986%
# 문제
# N(1 ≤ N ≤ 100,000)개의 로프가 있다. 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.

# 하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

# 각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오. 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.

# 입력
# 첫째 줄에 정수 N이 주어진다. 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다. 이 값은 10,000을 넘지 않는 자연수이다.

# 출력
# 첫째 줄에 답을 출력한다.

import sys
input = sys.stdin.readline


def solution(N:int, data:list):
    
    data.sort()
    max_w = 0

    for i in range(N):
        d_sum = data[i] * (N-i)
        if max_w < d_sum:
            max_w = d_sum

    print(max_w)

    # max_w = 0

    # for i in range(N):
    #     if max_w < min(data[i:])*(N-i):
    #         max_w = min(data[i:])*(N-i)
    
    # print(max_w)

# 시간초과, 시간복잡도는 O(N)
# 시간제한이 2초
# min함수 사용으로 매번 최소값을 구하고 빼주니 시간초과가 발생
# 리스트 정렬로 매번 최소값을 구할 필요가 없게 만들었다.


if __name__ == "__main__":
    N = int(input())
    data = [int(input()) for _ in range(N)]

#    print(data)
    solution(N, data)



