# 2563문제
# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.



# 예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다.

# 입력
# 첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다

# 출력
# 첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.




def solution(S:list, area:list):
    result = 0


    for i in S:
        for k in range(i[0], i[0]+10):
            for j in range(i[1], i[1]+10):
#                print("j and k : " + f"{j} {k}")
                area[j][k] = 1
    
    # for i in area:
    #     print(i)
    result = 0
    for i in area:
        result += i.count(1)
    print(result)
    
if __name__ == "__main__":
    S = []
    N = int(input())
    area = [[0 for x in range(100)]for y in range(100)]

    # for i in area:
    #     print(i)
    
    for i in range(N):
        S.append(list(map(int, input().split())))

    solution(S, area)




"""
back7_4는 겹치는 부분을 충돌계산으로 색종이 100넓이 * N에서 겹넓이를 빼는 방식이었다면,
back7_4_1에서는 모든 영역을 0으로 놓고 색종이를 붙인 공간을 1로 바꾸어
counting 하는 방식이다.

"""
