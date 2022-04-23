'''
균형잡힌 세상(4949)
푼 날자:2022-04-19-11:26
1
'''
import sys
sys.stdin = open('input.txt')
lines = list(sys.stdin.readlines())

# def checker(li):
#     gualho = ['(',')','{','}','[',']']
#     for i in gualho:
#         if not i in li:
#             pass
#         else:
#             return a

# for val in lines:
#     while gualho. in val:
#         if '(' in val:
#             if ')' in val[val.index('('):]:
#                 val.pop('(')
#                 val.pop(')')
#             else:
#                 val.pop('(')
#                 print('no')
#                 break
#         if ')' in val:
#             if '(' in val[val.index(')'):]:
#                 val.pop('(')
#                 val.pop(')')
#             else:
#                 val.pop(')')
#                 print('no')
#                 break

#         if '[' in val:
#             if ']' in val[val.index('['):]:
#                 val.pop('(')
#                 val.pop(')')
#             else:
#                 val.pop('[')
#                 print('no')
#                 break
#         if ']' in val:
#             if '[' in val[val.index(']'):]:
#                 val.pop('(')
#                 val.pop(')')
#             else:
#                 val.pop(']')
#                 print('no')
#                 break
#     print('yes')
