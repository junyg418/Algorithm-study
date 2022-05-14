'''
럭키 스트레이트(321p)
2022-05-14-12:57
1.12분 15초
'''
n = ' '.join(input())
nums = list(map(int, n.split(' ')))
half = len(nums)//2
if sum(nums[:half]) == sum(nums[half:]):
    print('LUCKY')
else:
    print('READY')