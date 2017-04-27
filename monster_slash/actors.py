from random import randint

class Actor:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = 100 * level

    def is_alive(self):
        return self.hp > 0

    def __repr__(self):
        return '<Actor: {}, Level: {}'.format(self.name, self.level)

    def get_attack_power(self):
        return randint(1,100) * self.level

    def attacks(self,other):
        raise NotImplementedError()

class Player(Actor):

    def heal(self):
        self.hp += 10

    def attacks(self, enemy):
        power = self.get_attack_power()
        print('{} attacks the {}.'.format(self.name, enemy.kind))
        print('{} has {} attack power'.format(self.name, power))
        enemy.hp -= power

class Enemy(Actor):
    def __init__(self, name, level, kind):
        super().__init__(name, level)
        self.kind = kind

    def attacks(self, player):
        e_power = self.get_attack_power()
        print('{} the {} attacks {}.'.format(self.name, self.kind, player.name))
        print('{} has {} attack power.'.format(self.name, e_power))
        player.hp -= e_power


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
    oger = Ogre(name='Bob', level = 1, size= 2)
    print(player.hp)
    oger.attacks(player)
    print(player.hp)

    player.heal()
    print(player.hp)
