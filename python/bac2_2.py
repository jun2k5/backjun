# 9498문제
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 시험 성적을 출력한다.

def solution():
    N = int(input())            #입력
    if N >= 90:
        print("A")              #90점 이상이면 A출력
    elif N < 90 and N >= 80:
        print("B")              #80점 이상이면 B출력
    elif N < 80 and N >= 70:
        print("C")              #70점 이상이면 C출력
    elif N < 70 and N >= 60:
        print("D")              #60점 이상이면 D출력
    else:
        print("F")              #그외 점수 F출력

if __name__ == "__main__":
    solution()


"""
-Learning Point
    python은 switch문이 없다.


"""

