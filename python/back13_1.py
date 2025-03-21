def sort_numbers(numbers):
    """
    주어진 숫자 리스트를 오름차순으로 정렬하여 반환하는 함수
    
    Args:
        numbers (list): 정렬할 정수 리스트
        
    Returns:
        list: 오름차순으로 정렬된 리스트
    """
    # 여기에 정렬 로직을 구현하세요
    return sorted(numbers)

def main():
    # 수의 개수 N 입력 받기
    n = int(input())
    
    # N개의 수 입력 받기
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    
    # 정렬하기
    sorted_numbers = sort_numbers(numbers)
    
    # 결과 출력하기
    for num in sorted_numbers:
        print(num)

if __name__ == "__main__":
    main()
