import random

options= {'p': 'piatra',
          'f': 'foarfece',
          'h': 'hartie',
          'q': 'quit'
          }

def verificare(jucator, robot):
    if jucator == robot:
        return None
    elif jucator == 'h':
        if robot == 'f':
            return False
        else:
            return True
    elif jucator == 'p':
        if robot == 'h':
            return False
        else:
            return True
    elif jucator == 'f':
        if robot == 'p':
            return False
        else:
            return True

def game():
    while True:
        jucator = input(f'Introduceti optiunea: {options.keys()}')
        if jucator == 'q':
            break
        if jucator not in ['p','f','h']:
            print("Nu e printre optiuni")
            continue
        robot = random.choice('pfh')
        result = verificare(jucator, robot)
        print(f'robotul a ales {robot}')
        if result is True:
            print('Avem un castigator!')
        elif result is False:
            print("Ai pierdut!")
        else:
            print("EGAL")

if __name__ == '__main__':
    game()

