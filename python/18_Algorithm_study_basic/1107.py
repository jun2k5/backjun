# 리모컨
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	123656	31196	22004	23.632%
# 문제
# 수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

# 수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.

# 수빈이가 지금 보고 있는 채널은 100번이다.

# 입력
# 첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.

# 출력
# 첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.


import sys
input = sys.stdin.readline

def solution(now_channel:int , N:int, M:int, break_buttons:list):
    # 현재 채널에서 N으로 이동하는데 필요한 최소 버튼 수
    min_button_count = abs(now_channel - N)

    # 고장난 버튼이 없는 경우
    if M == 0:
        print(min_button_count)
        return

    for nums in range(1000001):
        nums = str(nums)

        for j in range(len(nums)):
            # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
            if int(nums[j]) in break_buttons:
                break

            # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
            elif j == len(nums) - 1:
                min_button_count = min(min_button_count, abs(int(nums) - N) + len(nums))

    print(min_button_count)

if __name__ == "__main__":
    now_channel = 100
    N = int(input())
    M = int(input())
    break_buttons = list(map(int, input().split()))

    solution(now_channel, N, M, break_buttons)

