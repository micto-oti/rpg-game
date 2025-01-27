import random as r

class Enemy:
    def __init__(self, name, attack, defense, health, exp_reward):
        self.name = name
        self.dmg = attack
        self.res = defense
        self.hp = health
        self.exp = exp_reward

    def is_alive(self):
        return self.hp > 0

# Враги
enemies_Tier1 = [
    Enemy("Старая леди", attack=5, defense=2, health=10, exp_reward=3),
    Enemy("Масочник", attack=7, defense=3, health=15, exp_reward=4),
    Enemy("Раскаяние", attack=3, defense=3, health=14, exp_reward=4)
]

enemies_Tier2 = [
    Enemy("Не прикасайся ко мне", attack=11, defense=4, health=36, exp_reward=8),
    Enemy("Большая птица", attack=9, defense=6, health=27, exp_reward=7),
    Enemy("Маленький принц", attack=9, defense=5, health=30, exp_reward=8)
]

enemies_Tier3 = [
    Enemy("Балерины близняшки", attack=13, defense=10, health=55, exp_reward=10),
    Enemy("Королева ненависти", attack=17, defense=9, health=60, exp_reward=11),
    Enemy("Там ничего нет", attack=15, defense=11, health=58, exp_reward=10)
]

def Tier1_recall():
    return enemies_Tier1


def Tier2_recall():
    return enemies_Tier2
Ы
def Tier3_recall():
    return enemies_Tier3