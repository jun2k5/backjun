# 11654문제
# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

# 입력
# 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

# 출력
# 입력으로 주어진 글자의 아스키 코드 값을 출력한다.

if __name__ == "__main__":
    #문제 입력, S가 char형으로 들어올 수 있는 길이 1일때까지 
    while(1):
        try:
            S = input()
        except:
            print("오류")

        if len(S) == 1:        
            break

    #아스키코드 숫자 출력
    print(ord(S))

    #아스키코드 숫자의 아스키코드 문자 출력
#    print(chr(ord(S)))

"""
-Learning Point
ord()함수를 사용하면 한 개의 문자를 받아 아스키코드 숫자를 추출해준다.
chr()함수를 사용하면 한 개의 정수를 받아 해당하는 아스키코드 문자를 추출해준다.
"""
