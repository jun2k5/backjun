# 소트인사이드
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	113710	74720	61456	66.008%
# 문제
# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

# 입력
# 첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.



if __name__ == "__main__":

######### sort함수 사용 ###############
    # data = list(input())

    # data.sort(reverse=True)

    # for i in data:
    #     print(i, end='')


############ 계수정렬 #################
    data = list(input())
    count = [0] * 10

    for i in range(len(data)):
        count[int(data[i])] += 1
    
#    print(count)

    for j in range(10):
        if count[9-j] != 0:
            for k in range(count[9-j]):
                print(9-j, end='')





