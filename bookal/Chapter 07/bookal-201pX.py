'''
Chapter 07 이진 탐색
2022-05-03-00:48
알고리즘 책 201p
떡볶이 떡 만들기|난이도 중|풀이시간 40분|
1. 1차시도 실패
2. 함수모형으로 풀이보고 작성
'''
n, m = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        sumval = 0
        for i in array:
            if i>mid:
                sumval += i-mid
        if sumval == target:
            return mid
        elif sumval >= target:
            start = mid + 1
        else:
            end = mid -1
    return None

start = 0
end = max(array)
result = binary_search(array, m, start, end)
print(result)




# 1차시도 -> 실패
# n, m = map(int, input().split())
# dducks = list(map(int, input().split()))

# def binary_serach(array, m, start, end):
#     if start> end:
#         return None
#     cal_array = array[:]
#     giveduck = sum(cal_array)-len(cal_array)*((start+end)//2)

#     mid = (start+end)//2
#     if  m == giveduck:
#         return mid
#     elif giveduck < m:
#         return binary_serach(array, m, 0, mid-1)
#     else:
#         return binary_serach(array, m , mid+1, end)

# while True:
#     result = binary_serach(dducks, m, 0, n)
#     if result == None:
#         m += 1
#         binary_serach(dducks, m, 0, n)
#     else:
#         print(result)
#         break
