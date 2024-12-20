import random
import time

# Global Variables
player_list = []

# Constant Variables
SCORES = {'Full House': 25,
          'Small Straight': 30,
          'Large Straight': 40,
          'Yahtzee': 50}


class Text:
    WARNING = '\033[91m' # Red | Player 1
    COMPLETED = '\033[92m' # Green | Player 2
    INPUT = '\033[93m' # Yellow | Player 3
    MESSAGE = '\033[94m' # Blue | Player 4
    HINT = '\033[95m' # Magenta | Player 5
    STANDARD = '\033[0m'
    CHECKMARK = '✓'
    PLAYER_COLORS = [WARNING, COMPLETED, INPUT, MESSAGE, HINT] # 1 2 3 4 5


class Player:
    def __init__(self, player_number: int) -> None:
        self.player_number = player_number
        self.score_card = {'1': 0,
                      '2': 0,
                      '3': 0,
                      '4': 0,
                      '5': 0,
                      '6': 0,
                      '3_kind': [],
                      '4_kind': [],
                      'chance': []}
        self.color = Text.PLAYER_COLORS[player_number - 1]

    def roll_dice(self) -> list:
        return [random.randint(1, 6) for i in range(5)]

    def check_roll_eligibility(self, roll):
        pass

    def add_score(self, choice, roll):
        pass


class Msgs:
    # Game Loop Messages

    # Misc. Messages
    EXIT = f"\n{Text.COMPLETED}[✓]{Text.STANDARD} Goodbye!"

    # Error Messages
    VALUE_ERROR = f"\n{Text.WARNING}[!]{Text.STANDARD} A value you have entered caused an error..."
    TOO_MANY_PLAYERS = f"\n{Text.WARNING}[!]{Text.STANDARD} Maximum of 5 players..."
    TOO_LITTLE_PLAYERS = f"\n{Text.WARNING}[!]{Text.STANDARD} Minimum of 2 players..."


def get_num_players() -> int:
    while True:
        num_players = input(f"\n{Text.INPUT}[!]{Text.STANDARD} How many people will be playing with you? {Text.HINT}[Minimum 2 players | Maximum 5 Players | -1 to quit]{Text.STANDARD}\n")

        if num_players == "-1":
            time.sleep(0.5)
            print(Msgs.EXIT)
            break

        try:
            num_players = int(num_players)

            if num_players > 5:
                print(Msgs.TOO_MANY_PLAYERS)
                time.sleep(0.5)
                continue

            if num_players < 2:
                print(Msgs.TOO_LITTLE_PLAYERS)
                time.sleep(0.5)
                continue

            return num_players

        except ValueError:
            print(Msgs.VALUE_ERROR)
            time.sleep(0.5)
            continue


def start_game() -> None:
    print(f"\n{Text.MESSAGE}[!]{Text.STANDARD}  Welcome to Python Yahtzee!  {Text.MESSAGE}[!]{Text.STANDARD}")
    time.sleep(0.5)

    num_players = get_num_players()

    for i in range(num_players):
        player = Player(i + 1)
        player_list.append((player, i + 1))

    game_loop(player_list)

def game_loop(players: list) -> None:
    while True:
        break

def main() -> None:
    start_game()


if __name__ == "__main__":
    main()
