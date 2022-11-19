from res.terrain.terrain import Terrain
from res.units.unit import Unit

class Swamp(Terrain):
    __symbol = "~"
    __temp_hp = -10
    __temp_hit = 0
    
    @property
    def hp_mod(self):
        return self.__temp_hp
    
    @property
    def hit_mod(self):
        return self.__temp_hit
    
    def change_unit(self, unit):
        if not(isinstance(unit, Unit)):
            raise ValueError("Юнит должен пренадлежать классу Unit")
        unit.change_unit(self.__temp_hp, self.__temp_hit)
    
    def to_string(self):
        return "\033[34m{}".format(self.__symbol) + " "