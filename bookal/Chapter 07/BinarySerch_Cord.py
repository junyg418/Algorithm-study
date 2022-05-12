#재귀합수로 구현한 이진 탐색코드
'''
2022-05-12 복습 정답완료
'''
def binary_search(array:list, target:int, start, end):
    '''
    array:배열
    target:찾으려고 하는 원소
    start:배열의 시작점의 인덱스
    end:배열의 끝점의 인덱스
    '''
    if start > end:
        return None
    # 중간점이 target이라면
    mid = (start+end)//2 #중간점의 인덱스
    if array[mid] == target:
        return target
    # 중간점의 값보다 찾고자 하는 값이 작은 경우->왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우->오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열)
n, target = map(int, input().split())
# 전체 원소 배열
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('결과가 존재하지 않습니다.')
else:
    print(result+1) # result는 index값이기에 몇번째를 물어보기에 + 1을 추가한다