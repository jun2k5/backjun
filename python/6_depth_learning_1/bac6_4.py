# 10988문제
# 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.

# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 

# level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

# 입력
# 첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

def solution(S:list):
    S_re = S.copy()
    S_re.reverse()
 #   print(S_re)
    if S == S_re:
        print("1")
        return
    print("0")


if __name__ == "__main__":
#    S = list(input())
#    print(S)
#    solution(S)
    S = [1,2,3]
    S_r = S
    S_r.reverse()


    print(S == S_r)

"""
-Learning Point
S = [1,2,3]
S_r = S
S_r.reverse()
print(S == S_sr)

라고 할 경우
S_r은 S의 주소를 가르키는 포인터변수기때문에


"""



