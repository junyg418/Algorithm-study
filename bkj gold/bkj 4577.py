# 2023-07-03 16:36 ~
# 4577 소코반

class Game:
    # URDL

    def __init__(self, row:int, column:int) -> bool:
        self.move_ch = {"U":0, "R":1, "D":2, "L":3}
        self.move_x = [-1, 0, 1, 0]
        self.move_y = [0, 1, 0, -1]

        self.game_map = [list(input()) for _ in range(row)]
        self.control = input()

        self.data__init__()
    
    def run(self):
        for move_data in self.control:
            turn_move = self.move_ch[move_data]
            play_x, play_y = self.player_pos
            play_goto_pos = [play_x+self.move_x[turn_move], play_y+self.move_y[turn_move]]
            play_goto = self.game_map[play_goto_pos[0]][play_goto_pos[1]]

            if play_goto == "#":
                pass
            elif play_goto == "b" or play_goto == "B":
                box_goto = self.game_map[play_goto_pos[0]+self.move_x[turn_move]][play_goto_pos[1]+self.move_y[turn_move]]
                if box_goto == "." or  box_goto == "+":
                    # player 상자 밀었는데 뒤 비어있을 떄
                    if self.player_pos in self.goal_pos_list:
                        self.game_map[self.player_pos[0]][self.player_pos[1]] = "+" # 원래 위치 변경 적용
                    else:
                        self.game_map[self.player_pos[0]][self.player_pos[1]] = "."

                    # player 위치 변경
                    self.player_pos = [play_goto_pos[0], play_goto_pos[1]] # 시스템적 플레이어 위치 변경
                    if play_goto_pos in self.goal_pos_list:
                        self.game_map[self.player_pos[0]][self.player_pos[1]] = "W"
                    else:
                        self.game_map[self.player_pos[0]][self.player_pos[1]] = "w"

                    tmp_box_idx = self.box_pos_list.index([play_goto_pos[0], play_goto_pos[1]]) # 기존 박스 위치
                    self.box_pos_list[tmp_box_idx] = [play_goto_pos[0]+self.move_x[turn_move], play_goto_pos[1]+self.move_y[turn_move]] # 박스 위치변경
                    if self.box_pos_list[tmp_box_idx] in self.goal_pos_list:
                        self.game_map[self.box_pos_list[tmp_box_idx][0]][self.box_pos_list[tmp_box_idx][1]] = "B"
                    else:
                        self.game_map[self.box_pos_list[tmp_box_idx][0]][self.box_pos_list[tmp_box_idx][1]] = "b"
                        
            elif play_goto == ".":
                if self.player_pos in self.goal_pos_list:
                    self.game_map[self.player_pos[0]][self.player_pos[1]] = "+" # 원래 위치 변경 적용
                else:
                    self.game_map[self.player_pos[0]][self.player_pos[1]] = "."
                self.player_pos = [play_goto_pos[0], play_goto_pos[1]] # 시스템적 플레이어 위치 변경
                self.game_map[self.player_pos[0]][self.player_pos[1]] = "w"

            elif play_goto == "+":
                if self.player_pos in self.goal_pos_list:
                    self.game_map[self.player_pos[0]][self.player_pos[1]] = "+" # 원래 위치 변경 적용
                else:
                    self.game_map[self.player_pos[0]][self.player_pos[1]] = "."
                self.player_pos = [play_goto_pos[0], play_goto_pos[1]] # 시스템적 플레이어 위치 변경
                self.game_map[self.player_pos[0]][self.player_pos[1]] = "W"
            
            if self.isfin():
                break



    def data__init__(self):
        self.player_pos = None
        self.box_pos_list = []
        self.goal_pos_list = []

        for row, game_data in enumerate(self.game_map):

            # 플레이어 초기화
            if ("w" in game_data) or ("W" in game_data):
                try:
                    data = game_data.index("w")
                    self.player_pos = [row, data]
                except:
                    pass

                try:
                    data = game_data.index("W")
                    self.player_pos = [row, data]
                    self.goal_pos_list.append([row, data])
                except:
                    pass
            
            # Box 초기화
            try:
                data = game_data.count("b")
                tmp_data = game_data
                tmp_count = 0
                for _ in range(data):
                    c_pos = tmp_data.index("b")
                    self.box_pos_list.append([row, c_pos+tmp_count])
                    tmp_data = tmp_data[c_pos+1:]
                    tmp_count += c_pos+1
            except:
                pass
            
            try:
                data = game_data.count("B")
                tmp_data = game_data
                tmp_count = 0
                for _ in range(data):
                    c_pos = tmp_data.index("B")
                    self.box_pos_list.append([row, c_pos+tmp_count])
                    self.goal_pos_list.append([row, c_pos+tmp_count])
                    tmp_data = tmp_data[c_pos+1:]
                    tmp_count += c_pos+1
            except:
                pass

            # 목표점 초기화
            try:
                data = game_data.count("+")
                tmp_data = game_data
                tmp_count = 0
                for _ in range(data):
                    c_pos = tmp_data.index("+")
                    self.goal_pos_list.append([row, c_pos+tmp_count])
                    tmp_data = tmp_data[c_pos+1:]
                    tmp_count += c_pos+1
            except:
                pass

    def isfin(self):
        for map_data in self.game_map:
            if "b" in map_data:
                return False
        return True

time = 1
while True:
    row, column = map(int, input().split())
    if not(row or column):
        break
    g = Game(row, column)
    g.run()
    if g.isfin():
        print(f"Game {time}: complete")
    else:
        print(f"Game {time}: incomplete")
    
    for map_data in g.game_map:
        print("".join(map_data))
    
    time += 1