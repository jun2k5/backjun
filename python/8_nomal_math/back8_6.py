# 1193문제
# 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

# 1/1	1/2	1/3	1/4	1/5	…
# 2/1	2/2	2/3	2/4	…	…
# 3/1	3/2	3/3	…	…	…
# 4/1	4/2	…	…	…	…
# 5/1	…	…	…	…	…
# …	…	…	…	…	…
# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

# 출력
# 첫째 줄에 분수를 출력한다.

"""
0   1,1

1   1,2     bm += 1
2   2,1     bj += 1 bm -= 1 False

3   3,1     bj += 1 bm -= 1 False
4   2,2     bj -= 1 bm += 1 Ture
5   1,3     

6   1,4
7   2,3
8   3,2
9   4,1

10  5,1
11  4,2
12  3,3
13  2,4
14  1,5
"""


def solution(S:int):
    bunja = 1
    bunmo = 2
    maxN = 2
    #mod가 True 면 분자 -1 분모 +1, False면 분자 +1 분모 -1
    mod = True

    if S == 1:
        print("1/1")
        return
    
    for i in range(0,S-2):
        if bunmo == maxN:
            maxN = bunmo +1
            mod = False

        if bunja == maxN:
            maxN = bunja + 1
            mod = True

        if mod:
            bunja -= 1
            bunmo += 1
        else:
            bunja += 1
            bunmo -= 1

        if bunja == 0:
            bunja = 1
        if bunmo == 0:
            bunmo = 1

#        print("count : " + f"{i} "+f"{bunja}" + "/" +f"{bunmo}")

    print(f"{bunja}" + "/" +f"{bunmo}")
    return


if __name__ == "__main__":
    S = int(input())

    solution(S)




"""
Runtimeout 으로 실패

"""