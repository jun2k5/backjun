# 2563문제
# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.



# 예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다.

# 입력
# 첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다

# 출력
# 첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.




def solution(S:list, N:int):

    area = 100 * N
    pre_S = []
    sub_x = 0
    sub_y = 0


    for i in S:

        for j in range(0, len(pre_S)):
            print("j:"+f"{j}")
            if abs(pre_S[j][0] - i[0]) < 10 and abs(pre_S[j][1] - i[1]) < 10:
                print('x and i[0] = ' + f"{pre_S[j][0]}"+" "+f"{i[0]}")
                print('absxi = ' + f"{abs(pre_S[j][0] - i[0])}")
                sub_x = abs(pre_S[j][0] - i[0])
                print(sub_x)
                print('y and i[1] = ' + f"{pre_S[j][1]}"+" "+f"{i[1]}")
                print('absyi = ' + f"{abs(pre_S[j][1] - i[1])}")
                sub_y = abs(pre_S[j][1] - i[1])
                print(sub_y)
                print("subvalue : " +f"{(10-sub_x) * (10 - sub_y)}")
                area -= (10-sub_x) * (10 - sub_y)
                print("now area: " + f"{area}")
        pre_S.append([i[0],i[1]])
        print("nowpreSx : " + f"{pre_S}")

        
    
    print(area)


    """
        area : 100
        x : 3 13
        y : 7 17

        x : 5 15
        y : 2 12

        7 12 5
        5 13 8

        -40
        160

        3개가 겹칠때
        3 7
        5 2
        13 2

    """

    return

if __name__ == "__main__":
    S = []
    N = int(input())

    for i in range(0, N):
        S.append(list(map(int, input().split())))

    solution(S, N)




"""
내일 다시 풀어볼 것.

"""
