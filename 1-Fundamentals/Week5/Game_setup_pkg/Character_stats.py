class Character:
    def __init__(self, name, hp, damage, defense):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defense = defense

Warrior = Character("Warrior", 2000, 700, 200)
Mage = Character("Mage", 1200, 1200, 100)
Rogue = Character("Rogue", 1500, 650, 150)
Boss1 = Character("Boss #1", 5000, 400,200)
Boss2 = Character("Boss #2", 3000, 800,100)
Boss3 = Character("Boss #3", 10000, 300,800)
FinalBoss = Character("Final Boss", 15000, 600,200)

