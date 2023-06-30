class Game:
    def __init__(self) -> None:
        self.passed_turn = 0
        self.map_size = tuple(map(int, input().split()))

        self.map = Map(self.map_size) # 지도 초기화

        self.player_spawn_point = self.map.player_start_pos  # 값 변경 X
        self.player_control = input()
        self.PLAYER = Player()
        
        self.boss_spawn_point = self.map.boss_start_pos # 값 변경 X

        self.monster_count = self.map.monster_count
        self.chest_count = self.map.chest_count

        # 몬스터 데이터 초기화
        self.monster_data_dic = {}
        for _ in range(self.monster_count):
            input_row, input_column, input_name, *input_data  = input().split()
            input_atk, input_defense, input_hp, input_exp = list(map(int, input_data))
            kwargs={
                "name":input_name,
                "atk":input_atk,
                "defense":input_defense,
                "hp":input_hp,
                "exp":input_exp
            }
            pos = (int(input_row)-1, int(input_column)-1) # 조정된 좌표
            if self.boss_spawn_point == pos:
                monster = BossMonseter(**kwargs)
            else:
                monster = Monster(**kwargs)
            self.monster_data_dic[pos] = monster
        
        # 상자 데이터 초기화
        self.chest_data_dic = {}
        for _ in range(self.chest_count):
            input_row, input_column, input_item_type, input_item_info = input().split()
            chest = Chest(item_type=input_item_type, info=input_item_info)
            pos = (int(input_row)-1, int(input_column)-1)
            self.chest_data_dic[pos] = chest
        
        self.map.init_objectField(self.monster_data_dic, self.chest_data_dic)
        self.object_map = self.map.object_field
        self.current_map = self.map.field
    
        self.move_object = Move(self.player_control, self.player_spawn_point, self.map.wall_coordinate_list, self.map_size)
        self.move_data = self.move_object.move_process_data


    def run(self):
        for pos in self.move_data:
            turn_reuslt = self.turnPass(pos)
            if type(turn_reuslt) == str: # str : 죽었을 때
                if self.resurrection(): # 부활 시도
                    self.run()
                    return
                else: # 게임 종료
                    self.endGame(turn_reuslt, pos)
                    return

            elif type(turn_reuslt) == bool:
                if turn_reuslt: # True : 보스 죽임
                    self.endGame(True, pos)
                    return
            
        self.endGame(False, pos)


    def turnPass(self, current_pos:tuple):
        """
        :return:
            None / 아무일도 없었다
            str / 죽음 -> resurrection 호출 해야함
            bool / True -> 보스 죽임
        """
        turn_result = None

        self.passed_turn += 1
        object_data = self.object_map[current_pos[0]][current_pos[1]]


        if type(object_data) == int:
            pass

        elif type(object_data) == Monster: # 몬스터와 싸움
            current_monster = self.monster_data_dic[current_pos]
            if self.current_map[current_pos[0]][current_pos[1]] != ".":
                if current_monster.run(self.PLAYER): # return value killed: bool | True -> 플레이어가 죽임 / False -> 플레이어가 죽음
                    exp = current_monster.EXP
                    if "EX" in self.PLAYER.accessories_list:
                        exp = int(exp*1.2)
                    
                    self.PLAYER.EXP += exp
                    self.current_map[current_pos[0]] = self.changeStrValue(self.current_map[current_pos[0]], current_pos[1], ".")
                    # self.current_map[current_pos[0]][current_pos[1]] = "."
                    
                    # RE 악세서리 연산
                    if "HR" in self.PLAYER.accessories_list:
                        self.PLAYER.current_hp += 3
                        if self.PLAYER.current_hp > self.PLAYER.HP:
                            self.PLAYER.current_hp = self.PLAYER.HP

                else: # 플레이어 사망
                    if self.PLAYER.current_hp < 0:
                        self.PLAYER.current_hp = 0
                    turn_result = current_monster.name

        elif type(object_data) == BossMonseter:
            if "HU" in self.PLAYER.accessories_list:
                self.PLAYER.current_hp = self.PLAYER.HP

            current_monster = self.monster_data_dic[current_pos]
            if current_monster.run(self.PLAYER): # return value killed: bool | True -> 플레이어가 죽임 / False -> 플레이어가 죽음
                exp = current_monster.EXP
                if "EX" in self.PLAYER.accessories_list:
                    exp = int(exp*1.2)
                
                self.PLAYER.EXP += exp
                self.current_map[current_pos[0]] = self.changeStrValue(self.current_map[current_pos[0]], current_pos[1], ".")
                # self.current_map[current_pos[0]][current_pos[1]] = "."
                
                # RE 장신구 연산
                if "HR" in self.PLAYER.accessories_list:
                    self.PLAYER.current_hp += 3
                    if self.PLAYER.current_hp > self.PLAYER.HP:
                        self.PLAYER.current_hp = self.PLAYER.HP

                turn_result = True # 게임 종료

            else: # 플레이어 사망
                turn_result = current_monster.name
        
        elif type(object_data) == Chest:
            current_chest = self.chest_data_dic[current_pos]
            if not current_chest.got_item:
                current_chest.getItem(self.PLAYER)
                current_chest.got_item = True
                self.current_map[current_pos[0]] = self.changeStrValue(self.current_map[current_pos[0]], current_pos[1], ".")
        
        elif type(object_data) == SpikeTrap:
            SpikeTrap.attak(self.PLAYER)
            if 0 >= self.PLAYER.current_hp:
                turn_result = "SPIKE TRAP"

        self.PLAYER.isLevelUp()
        return turn_result
    
    def changeStrValue(self, origin_value:str, index:int, change_value:str)->str:
        result = origin_value[:index] + change_value + origin_value[index+1:]
        return result

    def resurrection(self) -> bool:
        """
        :return:
            True / 부활 성공
            False / 부활 실패
        """
        if "RE" in self.PLAYER.accessories_list:
            self.player_control = self.player_control[self.passed_turn:]
            self.move_object = Move(self.player_control, self.player_spawn_point, self.map.wall_coordinate_list, self.map_size)
            self.move_data = self.move_object.move_process_data

            self.PLAYER.current_hp = self.PLAYER.HP
            self.PLAYER.accessories_list.remove("RE")
            return True
        else:
            return False
    
    def endGame(self, finish_by, last_pos:tuple):
        """
        :param finish_by:
            str / 죽임 당할 때
            bool -> True / 보스 처치했을 경우
            bool -> False / 입력 끝났을 경우
        """
        if self.PLAYER.current_hp < 0:
            self.PLAYER.current_hp = 0


        self.current_map[self.player_spawn_point[0]] = self.changeStrValue(self.current_map[self.player_spawn_point[0]], self.player_spawn_point[1], ".")
        if type(finish_by) != str:
            self.current_map[last_pos[0]] = self.changeStrValue(self.current_map[last_pos[0]], last_pos[1], "@")


        for row in self.current_map:
            print(row)
        print(f"Passed Turns : {self.passed_turn}")
        print(f"""LV : {self.PLAYER.LV}
HP : {self.PLAYER.current_hp}/{self.PLAYER.HP}
ATT : {self.PLAYER.ATK}+{self.PLAYER.weaponDamage}
DEF : {self.PLAYER.DEF}+{self.PLAYER.armorDefense}
EXP : {self.PLAYER.EXP}/{self.PLAYER.LV * 5}""")
        if type(finish_by) == str:
            print(f"YOU HAVE BEEN KILLED BY {finish_by}..")
        else:
            if finish_by:
                print("YOU WIN!")
            else:
                print("Press any key to continue.")


class Map:
    def __init__(self, coordinate:tuple) -> None:
        row, column = coordinate
        self.field = [input() for _ in range(row)]
        self.player_start_pos = (0, 0)
        self.boss_start_pos = (0, 0)
        self.wall_coordinate_list = []
        
        self.monster_count = 1
        self.chest_count = 0
        """
        object_field
        int {
          0 : None,
          -1 : wall
        }
        Monster : Monster 객체
        SpikeTrap :SpikeTrap 객체
        """
        self.object_field = [[0 for _ in range(column)] for _ in range(row)] 

        for x, map_string_data in enumerate(self.field):
            if (y:=map_string_data.find("@")) != -1:
                self.player_start_pos = (x, y) # player 시작 좌표 초기화
            if (y:=map_string_data.find("M")) != -1:
                self.boss_start_pos = (x, y) # boss 시작 좌표 초기화
            for object_data in map_string_data:
                if object_data == ".":
                    pass
                elif object_data == "&":
                    self.monster_count += 1

                elif object_data == "B":
                    self.chest_count += 1
    
    def init_objectField(self, monster_data:dict, chest_data:dict)->None:
        self.object_field[self.player_start_pos[0]][self.player_start_pos[1]] = 0
        for x, map_string_data in enumerate(self.field):
            for y, object_data in enumerate(map_string_data):
                if object_data == ".":
                    self.object_field[x][y] = 0
                elif object_data == "&":
                    self.object_field[x][y] = monster_data[(x,y)]
                elif object_data == "B":
                    self.object_field[x][y] = chest_data[(x,y)]
                elif object_data == "#":
                    self.object_field[x][y] = -1 # 벽을 나타냄 
                    self.wall_coordinate_list.append((x,y))
                elif object_data == "^":
                    self.object_field[x][y] = SpikeTrap()
                elif object_data == "M":
                    self.object_field[x][y] = monster_data[(x,y)]
            


class Player:
    def __init__(self) -> None:
        self.LV = 1  # 레벨
        self.HP = 20 # 체력
        self.ATK = 2 # 공격력
        self.DEF = 2 # 방어력
        self.EXP = 0 # 경험치

        self.current_hp = 20 # 현재 체력

        self.weaponDamage = 0
        self.armorDefense = 0
        self.accessories_list = []
    
    def getDefense(self):
        defense = self.DEF + self.armorDefense
        return defense

    def getAttack(self):
        attack = self.ATK + self.weaponDamage
        return attack

    def isLevelUp(self) -> None:
        """
        레벨 올리기 및 확인 하는 함수
        """
        # need_exp = 5 * self.LV
        while self.EXP >= (5 * self.LV): # 경험치 확인
            self.EXP = 0
            self.LV += 1
            self.ATK += 2
            self.DEF += 2
            self.HP += 5
            self.current_hp = self.HP # 체력 모두 회복
        


class Move:
    def __init__(self, move_data:str, start_pos:tuple, wall_list:list, map_size:tuple) -> None: #TODO 벽 위치도 받아야할듯 
        # TODO 나중에 RE 장신구 때문에 다시 연산해야할 수 있을듯 턴수로 데이터 재가공
        """
        :param move_data:
            string -> 입력한 이동 이동 데이터
        :param start_pos:
            tuple -> 플레이어의 시작 좌표
        Up : 0
        Right : 1
        Down : 2
        Left : 3
        """
        self.player_pos = start_pos
        self.wall_list = wall_list
        self.map_size = map_size

        self.move_encryption_data = []
        self.move_process_data = [] # result # tuple list
        
        self.x_control_data = [-1, 0, 1, 0]
        self.y_control_data = [0, 1, 0, -1]

        for string_data in move_data:
            if string_data == "U":
                self.move_encryption_data.append(0)
            elif string_data == "R":
                self.move_encryption_data.append(1)
            elif string_data == "D":
                self.move_encryption_data.append(2)
            elif string_data == "L":
                self.move_encryption_data.append(3)
        
        self.calculateMovement()

    def calculateMovement(self)-> None:
        tmp_pos = self.player_pos
        for move_data in self.move_encryption_data:
            origin_pos = tmp_pos
            tmp_x, tmp_y = tmp_pos
            tmp_pos = (tmp_x+ self.x_control_data[move_data], tmp_y+self.y_control_data[move_data])
            if tmp_pos in self.wall_list:
                tmp_pos = origin_pos
                self.move_process_data.append(tmp_pos)
                continue
            if tmp_pos[0] < 0 or tmp_pos[1] < 0:
                tmp_pos = origin_pos
                self.move_process_data.append(tmp_pos)
                continue
            elif tmp_pos[0] >= self.map_size[0] or tmp_pos[1] >= self.map_size[1]:
                tmp_pos = origin_pos
                self.move_process_data.append(tmp_pos)
                continue
            self.move_process_data.append(tmp_pos)


class SpikeTrap:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def attak(player:Player):
        damage = 5
        if "DX" in player.accessories_list:
            damage = 1
        player.current_hp -= damage
        

class Chest:
    def __init__(self, item_type:str, info) -> None:
        """
        :param item_type:
            str -> 무기 종류
            W : 무기
            A : 방어구
            O : 장신구
        """
        self.item_type = item_type
        self.info = info
        self.got_item = False

    def getItem(self, player:Player)->None:
        """
        :return:
            True : 정상작동
            False : 엑사서리 얻지 못함 (중복)
        """
        if self.item_type == "W":
            # if (player.weaponDamage) == 0: # 무기 덮어쓰기 때문에 주석처리
            player.weaponDamage = int(self.info)
        elif self.item_type == "A":
            # if (player.armorDefense) == 0:
            player.armorDefense = int(self.info)
        elif self.item_type == "O":
            if len(player.accessories_list) < 4:
                if self.info in player.accessories_list:
                    # if self.info == "CU":
                    #     player.accessories_list.append(self.info)
                    pass
                else:
                    player.accessories_list.append(self.info)

class Monster:
    def __init__(self, name:str, atk:int, defense:int, hp:int, exp:int) -> None:
        """
        :param name:
            str / 이름
        :param atk:
            int / 공격력
        :param defense:
            int / 방어력
        :param hp:
            int / 체력
        :param exp:
            int 주는 경험치
        """
        self.name = name
        self.ATK = atk
        self.DEF = defense
        self.HP = hp
        self.EXP = exp

        self.killed = False # 몬스터를 죽이지 못했다면 false 를 반환

    def attack(self, player:Player)->None:
        damage = max(1, self.ATK - player.getDefense()) # 데미지 계산식 max(1, atk-def)
        player.current_hp -= damage
        
    
    def run(self, player:Player) -> bool:
        """
        :param player:
            Player / 플래이어 객체
        :return:
            플래이어가 이겼다면   True 를 반환
            플래이어가 패배했다면 False를 반환
        """
        damage_stack = []
        damage_multiple = 1
        if not damage_stack: #이거 왜 썼었을까 not으로 변경함
            if "CO" in player.accessories_list:
                damage_multiple = 2
                if "DX" in player.accessories_list:
                    damage_multiple = 3
                
        damage = max(1, player.getAttack()*damage_multiple - self.DEF)
        damage_stack.append(damage)

        while(self.HP > sum(damage_stack)):
            self.attack(player) # 몬스터가 공격
            if player.current_hp <= 0:
                return self.killed

            damage = max(1, player.getAttack() - self.DEF) # 플레이어가 공격
            damage_stack.append(damage)

        self.killed = True
        return self.killed

                
        
class BossMonseter(Monster):
    def __init__(self, name: str, atk: int, defense: int, hp: int, exp: int) -> None:
        super().__init__(name, atk, defense, hp, exp)
    
    def run(self, player: Player) -> bool:
        """
        :param player:
            Player / 플래이어 객체
        :return:
            플래이어가 이겼다면   True 를 반환
            플래이어가 패배했다면 False를 반환
        """
        damage_stack = []
        damage_multiple = 1
        if not damage_stack:
            if "CO" in player.accessories_list:
                damage_multiple = 2
                if "DX" in player.accessories_list:
                    damage_multiple = 3
                
        damage = max(1, player.getAttack()*damage_multiple - self.DEF)
        damage_stack.append(damage)
        if self.HP <= damage:
            return True # 보스 죽음
        
        # 보스 공격 -> HU 장신구 때문
        if "HU" in player.accessories_list:
            pass # 첫공격 무효
        else:
            self.attack(player)
            if player.current_hp <= 0:
                return self.killed
        
        while(True):
            # 플레이어가 공격
            damage = max(1, player.getAttack() - self.DEF)
            damage_stack.append(damage)
            if self.HP <= sum(damage_stack):
                break
            
            # 몬스터가 공격
            self.attack(player) 
            if player.current_hp <= 0:
                return self.killed

        self.killed = True
        return self.killed

    def attack(self, player: Player):
        return super().attack(player)


g = Game()
g.run()