# 2739문제
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

# 입력
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

# 출력
# 출력형식과 같게 N*1부터 N*9까지 출력한다.


def solution():
    #입력
    N = int(input())

    #구구단 for문
    for i in range(1, 10):
        print(str(N) + " * " + str(i) +" = " + str(N * i))


if __name__ == "__main__":
    solution()


"""
-Learning Point
Python에서는 for-in 구문과 range()함수나 범위를 사용하여 반복문을 작성한다.

"""