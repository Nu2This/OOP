from random import randint

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return '<Player: {} at Level {}>'.format(self.name, self.level)

    def get_attack_power(self):
        return randint(1,100) * self.level

class Enemy:
    def __init__(self, kind, level):
        self.kind = kind
        self.level = level

    def __repr__(self):
        return '<Enemy: {}>'.format(self.kind)

    def get_attack_power(self):
        return randint(1,100) * self.level

if __name__ == '__main__':
    player = Player(name="Hercules", level = 3)
    print(player)
    enemy = Enemy(kind="Ogre", level = 1)
    print(enemy)
    print(enemy.level)
    print(player.get_attack_power())
    print(enemy.get_attack_power())
