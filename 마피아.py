player = int(input())
point = input().split()
point = list(map(int,point))
def daynight(playercount):
    if playercount%2:
        return 'day'
    return 'night'

def gameplay(time):
    if time =='day':#아침일때 참가자 유죄지수 죽임
        point.index(max(point))
    else: #저녁일때 한명죽이고 유죄지수 바뀜
        pass

