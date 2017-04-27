from random import randint

class Actor:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return '<Actor: {}, Level: {}'.format(self.name, self.level)

    def get_attack_power(self):
        return randint(1,100) * self.level

    def attacks(self,other):
        raise NotImplementedError()

class Player(Actor):

    def attacks(self, enemy):
        power = self.get_attack_power()
        enemy_power = enemy.get_attack_power()

        print('You summon {} power units!'.format(power))
        print('{} the {} summons {} power units'.format(enemy.name, enemy.kind, enemy_power))

        if power >= enemy_power:
            print('You slay {} the {}'.format(enemy.name, enemy.kind))
            return True
        else:
            print('You were defeated')
            return False
class Enemy(Actor):
    def __init__(self, name, level, kind):
        super().__init__(name, level)
        self.kind = kind

class Ogre(Enemy):
    def __init__(self, name, level, size):
        super().__init__(name, level, 'Ogre')
        self.size = size

    def get_attack_power(self):
        return randint(1, 50) * (self.size * self.level)
    pass

class Imp(Enemy):
    def __init__(self, name, level):
        super().__init__(name, level, 'Imp')
    def get_attack_power(self):
        return super().get_attack_power() / 4

if __name__ == '__main__':
    player = Player(name="Hercules", level = 3)
    print(player)
    enemy = Enemy(kind="Ogre", level = 1)
    print(enemy)
    print(enemy.level)
    print(player.get_attack_power())
    print(enemy.get_attack_power())
