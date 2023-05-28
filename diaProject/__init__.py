from diaProject import Player


class Game:
    def __init__(self) -> None:
        self.passed_turn = 0
        self.map_size = tuple(map(int, input().split()))

        self.map = Map(self.map_size) # 지도 초기화

        self.player_spawn_point = self.map.player_start_pos  # 값 변경 X
        self.player_control = input()
        self.PLAYER = Player()
        
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
            monster = Monster(**kwargs)
            pos = (int(input_row)-1, int(input_column)-1)
            self.monster_data_dic[pos] = monster
        
        # 상자 데이터 초기화
        self.chest_data_dic = {}
        for _ in range(self.chest_count):
            input_row, input_column, input_item_type, input_item_info = input().split()
            chest = Chest(item_type=input_item_type, info=input_item_type)
            pos = (int(input_row)-1, int(input_column)-1)
            self.chest_data_dic[pos] = chest
        
        self.map.init_objectField(self.monster_data_dic, self.chest_data_dic)

    
        self.move_object = Move(self.player_control, self.player_spawn_point, self.map.wall_coordinate_list, self.map_size)
        self.move_data = self.move_object.calculateMovement()


    def turnPass(self):
        self.passed_turn += 1
        


    def resurrection(self):
        self.player_control[self.passed_turn:]
        self.move_object = Move(self.player_control, self.player_spawn_point, self.map.wall_coordinate_list, self.map_size)
        self.move_data = self.move_object.calculateMovement()
        self.PLAYER.accessories_list.remove("RE")



class Map:
    def __init__(self, coordinate:tuple) -> None:
        row, column = coordinate
        self.field = [input() for _ in range(row)]
        self.player_start_pos = (0, 0)
        self.boss_start_pos = (0, 0)
        self.wall_coordinate_list = []
        
        self.monster_count = 1
        self.chest_count = 0
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

    def isLevelUp(self) -> None:
        """
        레벨 올리기 및 확인 하는 함수
        """
        # need_exp = 5 * self.LV
        while self.EXP <= (5 * self.LV): # 경험치 확인
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
        self.move_process_data = [] # result
        
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

    def calculateMovement(self)-> list:
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



class Object:
    pass


class Blank:
    def __init__(self) -> None:
        pass
        

class Wall:
    def __init__(self) -> None:
        # self.pos = pos
        pass


class SpikeTrap:
    def __init__(self) -> None:
        # self.pos = pos
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
        if self.item_type == "W":
            if (weapon:=player.weaponDamage) == 0:
                weapon += int(self.info)
        elif self.item_type == "A":
            if (armor:=player.armorDefense) == 0:
                armor += int(self.info)
        elif self.item_type == "O":
            if len(player.accessories_list) <= 4:
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

        self.current_hp = hp

    def attack(self, player:Player):
        damage = self.ATK - player.getDefense()
        player


class BossMonseter(Monster):
    pass


class Accessories:
    def __init__(self, player:Player) -> None:
        self.player = player


class AccessoriesHR(Accessories):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def effect(self):
        self.player.current_hp += 3
        if self.player.current_hp > self.player.HP:
            self.player.current_hp = self.player.HP

class AccessoriesRE(Accessories):
    def __init__(self, player: Player) -> None:
        super().__init__(player)
    
    def effect(self):
        pass


class AccessoriesCO(Accessories):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def effect(self):
        pass

class AccessoriesEX(Accessories):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def effect(self):
        pass


class AccessoriesDX(Accessories):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def effect(self):
        pass


class AccessoriesHU(Accessories):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def effect(self):
        pass


class AccessoriesCU(Accessories):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def effect(self):
        pass



def test_case():
    if __name__ == "__main__":
        # map_test = Map(list(map(int, input().split())))
        # print(map_test.player_start_pos)
        # m = Move("RRRUULLULUDDDLDRDRDRRRURRULUULLU", )
        # print(m.move_process_data)
        g = Game()
        print(g.move_object.move_process_data)
        pass

test_case()
