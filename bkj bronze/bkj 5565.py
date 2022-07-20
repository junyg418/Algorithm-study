'''
영수증(5565)b3
2022-07-20
1.정답
'''
'''
첫쨰 줄- 10권의 총 가격
둘쨰줄부터 9권의 가격
'''
first_line = int(input())
book_price_list = [int(input()) for _ in range(9)]
print(first_line-sum(book_price_list))
