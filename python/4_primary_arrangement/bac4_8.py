# 3052문제
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

# 출력
# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

#For문을 사용하여 중복배열제거하는 함수
def solution(A: list):
    B = []

    for i in A:
        if i not in B:
            B.append(i)
#    print(B)
    print(len(B))

#set형변환을 사용하여 중복배열제거하는 함수
def solution1(A: list):
    return print(len(set(A)))

#dictionary형변환을 사용하여 중복배열제거하는 함수
def solution2(A: list)->int:
    return print(len(dict.fromkeys(A)))

if __name__ == "__main__":
    #입력값 10개를 받을 리스트
    A = []*10

    #문제 입력값
    for i in range(0, 10):
        A.append(int(input())%42)

    solution(A)
    solution1(A)
    solution2(A)

"""
-Learning Point
형변환으로 중복을 허용하지않는 자료구조로 바꾸면
배열 안의 중복값이 제거된다.

"""

