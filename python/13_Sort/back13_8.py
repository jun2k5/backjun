# 좌표 정렬하기
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	169310	82808	64548	48.822%
# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

# def ySort(data:list):
#     sortedData = []

#     for i in range(len(data)-1):
#         for j in range(i + 1, len(data)):
#             if data[i] > data[j]:
#                 data[i], data[j] = data[j], data[i]
        
# def solution(N:int, data:list):
   

#     for i in range(N):
#         print(f"{data[i][0]} " + f"{data[i][1]}")

def solution(N:int, data:list):

    data.sort(key = lambda x : (x[1], x[0]))

    for i in range(N):
        print(f"{data[i][0]} " + f"{data[i][1]}")

if __name__ == "__main__":
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    solution(N, data)


