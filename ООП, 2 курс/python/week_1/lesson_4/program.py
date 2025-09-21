import random

class Unit:
    def __init__(self, id, team):
        self.id = id
        self.team = team

class Soldier(Unit):
    def follow_hero(self, hero):
        print(f"Солдат {self.id} следует за героем {hero.id}")

class Hero(Unit):
    def up_level(self, level=1):
        self.level = level + 1
        print(f"Герой {self.id} повысил уровень до {self.level}")

hero1 = Hero(1, "Команда_1")
hero2 = Hero(2, "Команда_2")

soldiers_team1 = []
soldiers_team2 = []

for i in range (3, 13):
    soldier = Soldier(i, random.choice(["Команда_1", "Команда_2"]))
    if soldier.team == "Команда_1":
        soldiers_team1.append(soldier)
    else: 
        soldiers_team2.append(soldier)

print(f"Количество солдат в первой команде: {len(soldiers_team1)}")
print(f"Количество солдат во второй команде: {len(soldiers_team2)}")

if len(soldiers_team1) > len(soldiers_team2):
    hero1.up_level()
elif len(soldiers_team1) < len(soldiers_team2):
    hero2.up_level()
else:
    hero1.up_level()
    hero2.up_level()

soldiers_team1[0].follow_hero(hero1)
print(f"Идентификационный номер солдата: {soldiers_team1[0].id}, героя: {hero1.id}")