# 1330문제
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

# 출력
# 첫째 줄에 다음 세 가지 중 하나를 출력한다.

# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.
# 제한
# -10,000 ≤ A, B ≤ 10,000

# Al = range(6)
# Bl = list(range(5,0,-1))

def solution():
    A, B = map(int, input().split())
    if A > B:
        print(">")
    elif A == B:
        print("==")
    else:
        print("<")

if __name__ == "__main__":
    solution()

# def solution(A, B):
# #    A, B = map(int, input().split())
#     if A > B:
#         print(">")
#     elif A == B:
#         print("==")
#     else:
#         print("<")

# def if_solution(A, B):
# #    A, B = map(int, input().split())
#     if A > B:
#         print(">")
#     if A == B:
#         print("==")
#     if A < B:
#         print("<")

# def ifel_solution(A, B):
# #    A, B = map(int, input().split())

#     if A == B:
#         print("==")
#         return;

#     if A > B:
#         print(">")
#     else:
#         print("<")

# from timeit import default_timer as timer
# import datetime

# def TimeTest():
#     start = timer()
#     for A in Al:
#         for B in Bl:
#             solution(A, B)
#     end = timer()

#     sec = (end - start)
#     result = datetime.timedelta(seconds=sec)
#     print("if=elif-else time : " + str(result) + "sec")


    
# def if_TimeTest():
#     start = timer()
#     for A in Al:
#         for B in Bl:
#             if_solution(A, B)
#     end = timer()

#     sec = (end - start)
#     result = datetime.timedelta(seconds=sec)
#     print("if=if-if time : " + str(result))

# def ifel_TimeTest():
#     start = timer()
#     for A in Al:
#         for B in Bl:
#             ifel_solution(A, B)
#     end = timer()

#     sec = (end - start)
#     result = datetime.timedelta(seconds=sec)
#     print("if=if-else time : " + str(result))
    
    
#if __name__ == "__main__":
    #solution()
    #TimeTest()
    #if_TimeTest()

    #ifel_TimeTest()

"""
-Learning Point
    궁금증이 생겨
    timetest를 진행해보았다.
    인터넷 검색에 비슷한 실험을 한 사람을 발견했다.
    단순 == 연산은 if-if-if가 느린듯한데
    위 경우는 switch -case 문을 활용하는것이 낫지않을까?

    only one cycle

    if elif else
    <
    0:00:00.000120
    ==
    0:00:00.000132
    >
    0:00:00.000126
    ===================
    if if if
    <
    0:00:00.000064
    ==
    0:00:00.000092
    >
    0:00:00.000088
    ===================
    if if else
    <
    0:00:00.000086
    ==
    0:00:00.000100
    >
    0:00:00.000127

    
    25 cyle

    if elif else
    0:00:00.002099 sec
    ==============
    if if if
    0:00:00.002003 sec
    ============
    if if else
    0:00:00.002271 sec
    

"""







