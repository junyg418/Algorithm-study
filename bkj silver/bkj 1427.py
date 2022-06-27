'''
소트인사이드(1427)S5
2022-06-27
1.성공!
2.숏코딩
'''
# n = input()
# n9 = '9'*n.count('9')
# n8 = '8'*n.count('8')
# n7 = '7'*n.count('7')
# n6 = '6'*n.count('6')
# n5 = '5'*n.count('5')
# n4 = '4'*n.count('4')
# n3 = '3'*n.count('3')
# n2 = '2'*n.count('2')
# n1 = '1'*n.count('1')
# n0 = '0'*n.count('0')
# print(f'{n9}{n8}{n7}{n6}{n5}{n4}{n3}{n2}{n1}{n0}')
n=input()
print(''.join([str(s)*n.count(str(s)) for s in range(10)][::-1]))