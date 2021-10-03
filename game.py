import random
from enum import IntEnum


no = ['n','no']
yes = ['y','yes','yeah','yeup','yah']

class GameChoice(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


game_choices = [f"{gamechoice.name}[{gamechoice.value}]" for gamechoice in GameChoice]
choices_str = ", ".join(game_choices)

beats = {
    GameChoice.Rock: [GameChoice.Scissors, GameChoice.Lizard,], 
    GameChoice.Paper: [GameChoice.Rock, GameChoice.Spock, ],
    GameChoice.Scissors: [GameChoice.Paper, GameChoice.Lizard,],
    GameChoice.Lizard: [GameChoice.Spock, GameChoice.Paper, ],
    GameChoice.Spock: [GameChoice.Scissors, GameChoice.Rock, ],
}

game_actions = {
    (GameChoice.Rock, GameChoice.Scissors):'crushes',
    (GameChoice.Rock, GameChoice.Lizard):'crushes',
    (GameChoice.Paper, GameChoice.Rock):'covers',
    (GameChoice.Paper, GameChoice.Spock):'disproves',
    (GameChoice.Scissors, GameChoice.Paper):'cuts',
    (GameChoice.Scissors, GameChoice.Lizard):'decapitates',
    (GameChoice.Lizard, GameChoice.Paper):'eats',
    (GameChoice.Lizard, GameChoice.Spock):'poisons',
    (GameChoice.Spock, GameChoice.Scissors):'smashes',
    (GameChoice.Spock, GameChoice.Rock):'vaporizes',

}

def game_action(choice1, choice2):
    print(f"\t{choice1.name} {game_actions.get((choice1, choice2))} {choice2.name}")
    return


def winner_of_round(user_choice, computer_choice):
    if user_choice==computer_choice:
        print("\tIt's a tie")
        return (0,0)

    if computer_choice in beats.get(user_choice):
        game_action(user_choice, computer_choice)
        print("\tYou win!")
        return (1,0)

    game_action(computer_choice, user_choice)
    print("\tYou lose!")
    return (0,1)


def winner_of_game(user_final_score, computer_final_score):
    print("GAME STATS-->")
    print(f"\tYour score: {user_final_score}")
    print(f"\tAI score: {computer_final_score}")
    if user_final_score>computer_final_score:
        print("\tYOU WIN")
    if user_final_score<computer_final_score:
        print ("\tAI WINS")
    if user_final_score==computer_final_score:
        print("\tIT'S A TIE")


def main():
    user_score = []
    computer_score = []
    while True:
        try:
            value = input(f'Enter a choice ({choices_str})-- GO: ')
            user_choice = GameChoice(int(value))
        except ValueError:
            print(f"\tYou entered '{value}', which is not a valid choice; try again")
            continue

        value = random.randint(0, len(GameChoice)-1)
        computer_choice = GameChoice(value)
        
        print(f"\tYour choice: {user_choice.name}, AI choice: {computer_choice.name}")

        res = winner_of_round(user_choice=user_choice, computer_choice=computer_choice)

        user_score.append(res[0])
        computer_score.append(res[1])

        again = input('\nGo again? (y/n):')

        if again.lower() in no:
            print("*"*24)
            print("Game Over")
            winner_of_game(sum(user_score), sum(computer_score))
            break


if __name__ == "__main__":
    main()
