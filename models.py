# =================
# BASE CLASS
# =================

class Character:
    def __init__(self, char_id, name, level, base_hp, base_atk, crit_rate, crit_dmg):
        self.id = char_id
        self.name = name
        self.level = level
        self.base_hp = base_hp
        self.base_atk = base_atk
        self.crit_rate = crit_rate
        self.crit_damage = crit_dmg
    
    # método para calcular o dano
    def calculate_expected_dmg(self):
        crit_multiplier = 1 + (self.crit_rate / 100) * (self.crit_damage / 100)
        return self.base_atk * crit_multiplier
    
    def get_performance_report(self):
        return f"""
=====================================
  PERFORMANCE REPORT: {self.name}  
=====================================
Class Type: {self.__class__.__name__} | Level: {self.level}
Base Attack: {self.base_atk} | HP: {self.base_hp}
Crit Ratio: {self.crit_rate}% / {self.crit_damage}%
Expected Avg Dmg: {self.calculate_expected_dmg():.2f}
====================================="""
    
# ================ 
# classe filha 1 - DPS
# ================
class DPSCharacter(Character):
    def __init__(self, char_id, name, level, base_hp, base_atk, crit_rate, crit_dmg, elemental_bonus=0.15):
        # super() chama o construtor da classe mãe (Character) para reaproveitar o codigo)
        super().__init__(char_id, name, level, base_hp, base_atk, crit_rate, crit_dmg)
        self.elemental_bonus = elemental_bonus
    
    # Sobrescrevendo o calculo de dano para adicionar o dano elemental
    def calculate_expected_dmg(self):
        base_expected = super().calculate_expected_dmg()
        return base_expected * (1 + self.elemental_bonus)
    
# ================
# clase filha 2 - suporte
# ================
class SupportCharacter(Character):
    def __init__(self, char_id, name, level, base_hp, base_atk, crit_rate, crit_dmg, heal_bonus=0.20):
            super().__init__(char_id, name, level, base_hp, base_atk, crit_rate, crit_dmg)
            self.heal_bonus = heal_bonus
    
    # método exclusivo dos suportes, para calcular a força da cura/escudo
    def calculate_shield_strenght(self):
        return (self.base_hp * 0.25) * (1 + self.heal_bonus)