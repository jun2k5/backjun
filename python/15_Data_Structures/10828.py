# 스택
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 0.5 초 (추가 시간 없음)	256 MB	292960	110164	79728	38.342%
# 문제
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.


def push(L:list, X:int):
    L.append(X)

def pop(L:list):
    if len(L) == 0:
        return -1
    return L.pop()

def size(L:list):
    return len(L)

def empty(L:list):
    return 1 if len(L) == 0 else 0
    
def top(L:list):
    return L[-1] if len(L) > 0 else -1



def solution(N:int, data:list):
    stack = []

    for j in data:
        command = j.split()
        if not command: # 빈줄 처리
            continue        
        if command[0] == "push":
            if len(command) < 2: #숫자 미입력 처리
                continue
            push(stack, command[1])
        if command[0] == "pop":
            print(pop(stack))
        if command[0] == "size":
            print(size(stack))
        if command[0] == "empty":
            print(empty(stack))
        if command[0] == "top":
            print(top(stack))

if __name__ == "__main__":
    N = int(input())
    data = [input() for _ in range(N)]

    solution(N, data)





