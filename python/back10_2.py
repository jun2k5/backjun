# 1085문제
# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 x, y, w, h가 주어진다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다.

# 제한
# 1 ≤ w, h ≤ 1,000
# 1 ≤ x ≤ w-1
# 1 ≤ y ≤ h-1
# x, y, w, h는 정수

def solution(x:int,y:int,w:int,h:int) -> None:

    x_count = 0
    if x > w-x:
        x_count = w-x
    else:
        x_count = x

    y_count = 0
    if y > h-y:
        y_count = h-y
    else:
        y_count = y
    
    if x_count < y_count:
        print(x_count)
    else:
        print(y_count)

if __name__ == "__main__":
    x,y,w,h = map(int, input().split())

    solution(x,y,w,h)