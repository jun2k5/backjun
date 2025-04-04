# 버블 소트
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	512 MB	37140	10582	7298	30.792%
# 문제
# N개의 수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에 대해서 버블 소트를 수행할 때, Swap이 총 몇 번 발생하는지 알아내는 프로그램을 작성하시오.

# 버블 소트는 서로 인접해 있는 두 수를 바꿔가며 정렬하는 방법이다. 예를 들어 수열이 3 2 1 이었다고 하자. 이 경우에는 인접해 있는 3, 2가 바뀌어야 하므로 2 3 1 이 된다. 다음으로는 3, 1이 바뀌어야 하므로 2 1 3 이 된다. 다음에는 2, 1이 바뀌어야 하므로 1 2 3 이 된다. 그러면 더 이상 바꿔야 할 경우가 없으므로 정렬이 완료된다.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 500,000)이 주어진다. 다음 줄에는 N개의 정수로 A[1], A[2], …, A[N]이 주어진다. 각각의 A[i]는 0 ≤ |A[i]| ≤ 1,000,000,000의 범위에 들어있다.

# 출력
# 첫째 줄에 Swap 횟수를 출력한다

import sys
input = sys.stdin.readline

# def solution(N:int, data:list):
#     #버블솔트 구현
#     swp_cnt = 0
#     for i in range(0, N):
#         for j in range(0, N-i-1):
#             if data[j] > data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]
#                 swp_cnt += 1
# #                print(f"{swp_cnt}" + "-swp : " + f"{data}")

#     print(swp_cnt)
############ 시간초과 #############
#   위의 알고리즘은 O(N**2)의 시간복잡도를 가진다.
#   따라서 병합정렬을 통해 시간복잡도를 O(N logN)으로 변경해야한다.



def mergeSort(l:int, r:int):
    global swp_cnt, data

    if l < r:
        m = (l + r) // 2
        mergeSort(l,m)
        mergeSort(m+1,r)

        sl = []
        i, j = l, m + 1

        while i <= m and j <= r:
            if data[i] <= data[j]:
                sl.append(data[i])
                i += 1
            else:
                sl.append(data[j])
                j += 1
                swp_cnt += m - i + 1
        if i <= m:
            sl = sl + data[i:m+1]
        if j <= r:
            sl = sl + data[j:r+1]
        
        for x in range(len(sl)):
            data[l + x] = sl[x]


if __name__ == "__main__":
    swp_cnt = 0    
    N = int(input())
    data = list(map(int, input().split()))
#    print( data )
    mergeSort(0, N-1)
    print(swp_cnt)



#시간 초과




