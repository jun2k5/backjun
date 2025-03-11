# 1978문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

import math

def solution(N:int, S:list) -> None:
    #소수 숫자 집계
    count = 0
    #소수 확인
    isPrime = True

    #소수 찾아서 count 집계
    #소수는 0과 1을 제외한 자기 자신이외의 약수가 없는 수
    for i in S:
        #0과 1 제외
        if i == 0 or i == 1:
            continue
        #소수검사
        for j in range(2, int(math.sqrt(i) + 1 )):
            if i % j == 0:
                isPrime = False
                break
        #검사 통과
        if isPrime:
            count += 1
        #초기화
        isPrime = True

    print(count)            

    #소수 개수 출력


if __name__ == "__main__":
    N = int(input())
    S = list(map(int, input().split()))

    solution(N, S)


"""
-Leaning Point

sqrt함수 사용 테스트 결과
        메모리   시간
미사용 32412KB / 36ms
사용   34536KB / 36ms

N의 개수와 숫자가 크지않아서 차이가 없는것 같다
N이 커질수록 시간에서 유의미한 차이를 보일 것

"""




