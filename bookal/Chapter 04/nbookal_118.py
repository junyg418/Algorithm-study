# 2023-04-23 14:39 실패.... 1시간 풀이및 검토

n, m = map(int, input().split())
x, y, view = map(int, input().split())
player_state = [x, y, view]

game_map_data = [list(map(int, input().split())) for _ in range(n)]


def get_backpos(current_data):
    x_pos = current_data[0]
    y_pos = current_data[1]
    view_dir = current_data[2]

    if view_dir == 0:
        back_pos = (x_pos+1, y_pos)
    elif view_dir == 1:
        back_pos = (x_pos, y_pos-1)
    elif view_dir == 2:
        back_pos = (x_pos-1, y_pos)
    elif view_dir == 3:
        back_pos = (x_pos, y_pos+1)

    return back_pos

def get_leftpos(current_data):
    x_pos = current_data[0]
    y_pos = current_data[1]
    view_dir = current_data[2]

    if view_dir == 0:
        left_pos = (x_pos, y_pos-1)
    elif view_dir == 1:
        left_pos = (x_pos-1, y_pos)
    elif view_dir == 2:
        left_pos = (x_pos, y_pos+1)
    elif view_dir == 3:
        left_pos = (x_pos+1, y_pos)

    return left_pos


def is_sea(current_data, check_dir):
    if check_dir == 'left':
        x_pos, y_pos = get_leftpos(current_data)
        if game_map_data[x_pos][y_pos] == 1:
            return True
        else:
            return False
    
    elif check_dir == 'back':
        x_pos, y_pos = get_backpos(current_data)
        if game_map_data[x_pos][y_pos] == 1:
            return True
        else:
            return False

def is_comes(current_data):
    x_pos, y_pos = get_leftpos(current_data)
    if game_map_data[x_pos][y_pos] == 2:
        return True
    else:
        return False

def turn_left():
    view_state = player_state[2]
    if view_state == 0:
        player_state[2] = 3
    else:
        player_state[2] += -1
    

move_count = 0
# end = True
while True:
    for count in range(4):
        if not is_sea(player_state, 'left'):
            if not is_comes(player_state):
                game_map_data[player_state[0]][player_state[1]] = 2
                player_state[0], player_state[1] = get_leftpos(player_state)
                move_count += 1
                turn_left()
                break
        turn_left()
    else:
        if not is_sea(player_state, 'back'):
            break
        else:
            player_state[0], player_state[1] = get_backpos(player_state)
            move_count += 1
print(move_count)