import random
from actors import Player, Enemy

def main():
        print_intro()
        play()

def print_intro():
    print('''
        Monster Slash !!!
        Ready Player One?
        [Press Enter to Continue]
    ''')
    input()

def play():
    enemies = [
        Enemy('Ogre',1),
        Enemy('Imp',1)
    ]
    player = Player('Hercules',1)
    while True:
        next_enemy = random.choice(enemies)
        cmd = input('You see a {}, [r]un, [a]ttack, [p]ass?\n'.format(next_enemy.kind))
        if cmd == 'r':
            print('{} runs away!'.format(player.name))
        elif cmd == 'a':
            print('{} attacks the {}'.format(player.name, next_enemy.kind))
            if player.attacks(next_enemy):
                enemies.remove(next_enemy)
            else:
                print('{} hides to plan the next move'.format(player.name))
        elif cmd == 'p':
            print('You are still thinking about your next move...')
        else:
            print('Please choose a valid option')
        print()
        print('*'*30)
        print()

        if not enemies:
            print('You have won! Congrats!')
            break

if __name__ == '__main__':
    main()
