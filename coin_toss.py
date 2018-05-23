import random

def PlayCoinToss():
    print('Get ready for a game of chance!')
    choice = ['Heads', 'Tails']
    playerChoice = input('Pick a side Heads (H) or Tails (T)')
    result = random.choice(choice)

    if playerChoice == 'H' and result == 'Heads':
        print('You win!')

    elif playerChoice == 'T' and result == 'Tails':
        print('You win!')

    else:
        print('You lose!')

    cont = input('Do you wish to proceed? y/n')

    if cont == 'y':
        return PlayCoinToss()

    else:
        pass

