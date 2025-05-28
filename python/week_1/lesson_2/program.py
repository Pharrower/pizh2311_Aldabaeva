import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, target):
        damage = 20
        target.health -= damage
        print(f"{self.name} атаковал {target.name}. У {target.name} осталось {target.health} здоровья.")
    
    def is_alive(self):
        return self.health > 0
    
warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

while warrior1.is_alive() and warrior2.is_alive():
    attacker, defender = random.choice([(warrior1, warrior2), (warrior2, warrior1)])
    attacker.attack(defender)

if warrior1.is_alive():
    print(f"{warrior1.name} победил!")
else:
    print(f"{warrior2.name} победил!")
    