# 2675문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 
# 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 
# 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

def solution(S: list):
        for j in S[1]:
            for i in range(0, int(S[0])):
                print(j, end='')
        print()

if __name__ == "__main__":
    #문제 입력
    N = int(input())

    for i in range(0,N):
        S = input().split(' ')
        solution(S)


# ToDo. 11-17 : 5-6, 5-7 주석달것

"""
-Learning Point
이중배열의 개념
배열 안의 배열
"""

