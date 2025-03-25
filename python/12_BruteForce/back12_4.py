# 체스판 다시 칠하기
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	145080	73242	58231	50.398%
# 문제
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

# 출력
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.


def solution(N:int, M:int, m_data:list):
    chess_board_W =["WBWBWBWB",
                    "BWBWBWBW",
                    "WBWBWBWB",
                    "BWBWBWBW",
                    "WBWBWBWB",
                    "BWBWBWBW",
                    "WBWBWBWB",
                    "BWBWBWBW"]
    
    chess_board_B = ["BWBWBWBW",
                    "WBWBWBWB",
                    "BWBWBWBW",
                    "WBWBWBWB",
                    "BWBWBWBW",
                    "WBWBWBWB", 
                    "BWBWBWBW", 
                    "WBWBWBWB"]

    min_cnt = 65 # 8*8 = 64

    for i in range(0, N-7):
        for j in range(0, M-7):
            cnt_w = 0
            cnt_b = 0

            for p in range(0, 8):
                for q in range(0,8):
                    if m_data[i+p][j+q] != chess_board_W[p][q]:
                        cnt_w += 1
                    if m_data[i+p][j+q] != chess_board_B[p][q]:
                        cnt_b += 1
    
            min_cnt = min(min_cnt, cnt_w, cnt_b)

    print(min_cnt)


    # cnt_w = 0 #W로 시작할 때
    # cnt_b = 0 #B로 시작할 때

    # for i in range(0, N):
    #     for j in range(0, M):
    #     # i 가 짝수일때 W 
    #         if (i+j) % 2 == 0:
    #             if m_data[i][j] != ['W']:
    #                 cnt_w += 1
    #             else:
    #                 cnt_b += 1


    #         else:
    #             if m_data[i][j] != ['B']:
    #                 cnt_w += 1
    #             else:
    #                 cnt_b += 1


    # print("cnt_w : ", f"{cnt_w}")
    # print("cnt_b : ", f"{cnt_b}")

    # if cnt_w > cnt_b:
    #     print("cnt_b : ", f"{cnt_b}")
    # else:
    #     print("cnt_w : ", f"{cnt_w}")

    # for i in range(0, N):
    #     for j in range(0, M):
                # i 가 짝수일때 W 

            # if i == 0 and j == 0:
            #     if m_data[i][j] == ['W']:
            #         chk = True
            #         continue
            #     else:
            #         chk = False
            #         continue

            # if j == 0:
            #     if m_data[i-1][j] == ['W']: #위가 백색이면
            #         if m_data[i][j] == ['W']:
            #             cnt += 1
            #         chk = False
            #         continue

            #     if m_data[i-1][j] == ['B']: #위가 흑색이면
            #         if m_data[i][j] == ['B']:
            #             cnt += 1
            #         chk = True
            #         continue


            # if chk: #전거가 백색이면
            #     if m_data[i][j] == ['W'] :
            #         cnt += 1
            #     chk = False
            #     continue

            # else: #전거가 흑색이면
            #     if m_data[i][j] == ['B']:
            #         cnt += 1
            #     chk = True
            #     continue

    # print(cnt)


if __name__ == "__main__":
    N, M = map(int, input().split())
    m_data = [list(map(str, input())) for _ in range(N)]
    # print(m_data)
    # print(m_data[0][0])
    
    solution(N,M,m_data)



"""
문제를 잘못 읽어 20250324 시간초과
20250325에 다시 풀기

내일 8X8체스판으로 잘라내기 << 이 부분을 구현할 것

"""
