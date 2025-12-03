class GameCharacter:
    def __init__(self, hp, damage, armor):
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def take_damage(self, amount):
        real_damage = max(0, amount - self.armor)
        self.hp -= real_damage
        if self.hp < 0:
            self.hp = 0
