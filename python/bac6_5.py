# 1157문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

def solution(S:str):
    #입력값이 1보다 작으면 대문자 출력    
    if len(S) <= 1:
        print(S.upper())
        return

    #입력값 소문자화
    S_lo = S.lower()
    #history보관 배열선언
#     cache = []
#     #중복알파벳보관 배열선언
#     result = []
# #    print(S_lo)

#     #중복검사 For문``
#     for i in range(0, len(S_lo)):
#         #중복알파벳이면 result에 담기
#         if S_lo[i] in cache:
#             result.append(S_lo[i].upper())
#         #검사 후 캐쉬에 담기
#         cache.append(S_lo[i])


    #중복된 알파벳들 담은 result배열
 #   print(result)

    #중복 알파벳과 수를 alpa_D 딕셔너리에 종합
    alpa_D = {}
    for i in S_lo:
        try:
            alpa_D[i] += 1
        except:
            alpa_D[i] = 1
     
#    print(alpa_D)

    #최대 value값을 가진 key 리스트 생성
    end = [k for k,v in alpa_D.items() if max(alpa_D.values()) == v]

    if len(end) > 1:
        print("?")
        return

    print(end.pop())

if __name__ == "__main__":
    S = input()

    solution(S)