# 수 찾기
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	311067	100197	65869	30.706%
# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

import sys


def binary_search(arr:list, target:int):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
#            return mid
            return 1
        
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

    return 0    #존재하지 않으면 0출력

def solution(N:int, NL:list, M:int, ML:list):
    NL.sort()

    # for j in ML:      # in 사용시 Runtime 에러가 발생
    #     if j in NL:
    #         print(1)
    #     else:
    #         print(0)

    for j in ML:
        print(binary_search(NL, j))

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    n_data = sys.stdin.readline().split()
    M = int(sys.stdin.readline())
    m_data = sys.stdin.readline().split()

    solution(N, n_data, M, m_data)



"""
방법 1.

이진 탐색은 정렬된 배열에서만 사용 가능하다.
    변동이 적은 리스트에서
    정렬을 자주 안해도 되는 리스트에서 사용하면 효율적이다.
    O(logN)의 시간복잡도(time complexity)로 탐색해준다.

이진 탐색 방법:
    리스트의 처음과 끝을 반으로 나눠 인덱스 중간을 찾고
    인덱스 중간값과 타겟을 비교하여
    타겟값이 인덱스 중간값보다 크면 오른쪽 배열만 탐색
    작으면 왼쪽 배열만 탐색한다.
    이것을 반복한다.

"""
