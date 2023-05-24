class Game:
    def __init__(self) -> None:
        self.map = Map(tuple(map(int, input().split())))
        
        self.player_control = input()
        
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
            pos = (input_row, input_column)
            self.monster_data_dic[pos] = monster
        
        # 상자 데이터 초기화
        self.chest_data_dic = {}
        for _ in range(self.chest_count):
            input_row, input_column, input_item_type, input_item_info = input().split()
            chest = Chest(item_type=input_item_type, info=input_item_type)
            pos = (input_row, input_column)
            self.chest_data_dic[pos] = chest
            
        

class Map:
    def __init__(self, coordinate:tuple) -> None:
        row, column = coordinate
        self.field = [input() for _ in range(row)]

        self.monster_count = 0
        self.chest_count = 0
        # self.object_field = [[] for _ in range(row)]

        for map_string_data in self.field:
            for object_data in map_string_data:
                if object_data == ".":
                    pass
                elif object_data == "&":
                    self.monster_count += 1

                elif object_data == "B":
                    self.chest_count += 1



class Player:
    def __init__(self) -> None:
        self.LV = 1  # 레벨
        self.HP = 20 # 체력
        self.ATK = 2 # 공격력
        self.DEF = 2 # 방어력
        self.EXP = 0 # 경험치

        self.current_hp = 20 # 현재 체력
        self.weapon = False
        self.armor = False
        self.accessories_count = 0

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

    def attak(self, player:Player):
        damage = 5
        player.current_hp -= damage
        

class Chest:
    def __init__(self, item_type:str, info) -> None:
        self.item_type = item_type
        self.info = info

    def getItem(self)->None:
        pass


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
        player.accessories_count += 1


class AccessoriesHR(Accessories):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def effect(self):
        self.player.current_hp += 3
        if self.player.current_hp > self.player.HP:
            self.player.current_hp = self.player.HP