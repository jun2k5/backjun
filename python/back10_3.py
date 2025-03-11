# 3009문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.


def solution(S_x:list, S_y:list) -> None:
    lx = 0
    ly = 0

    if S_x[0] == S_x[1]:
        lx = S_x[2]

    elif S_x[0] == S_x[2]:
        lx = S_x[1]

    elif S_x[1] == S_x[2]:
        lx = S_x[0]

    if S_y[0] == S_y[1]:
        ly = S_y[2]

    elif S_y[0] == S_y[2]:
        ly = S_y[1]

    elif S_y[1] == S_y[2]:
        ly = S_y[0]

    print(f"{lx} {ly}")



if __name__ == "__main__":
    S_x = [] * 3
    S_y = [] * 3

    for i in range(0, 3):
        x, y = map(int, input().split())

        S_x.append(x)
        S_y.append(y)

    solution(S_x, S_y)







    