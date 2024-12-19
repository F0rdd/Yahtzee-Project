import dice
import time

class Text:
    WARNING = '\033[91m' # Red
    COMPLETED = '\033[92m' # Green
    INPUT = '\033[93m' # Yellow
    MESSAGE = '\033[94m' # Blue
    HINT = '\033[95m' # Magenta
    STANDARD = '\033[0m'
    CHECKMARK = '✓'

class Player:
    def __init__(self):
        pass

    def roll_dice(self):
        pass

    def check_roll_eligibility(self, roll):
        pass

    def score(self):
        pass

class Msgs:
    # Misc. Messages
    EXIT = f"\n{Text.COMPLETED}[✓]{Text.STANDARD} Goodbye!"

    # Error Messages
    VALUE_ERROR = f"\n{Text.WARNING}[!]{Text.STANDARD} A value you have entered caused an error..."
    TOO_MANY_PLAYERS = f"\n{Text.WARNING}[!]{Text.STANDARD} Maximum of 10 players..."
    TOO_LITTLE_PLAYERS = f"\n{Text.WARNING}[!]{Text.STANDARD} Minimum of 2 players..."

def get_num_players():
    while True:
        num_players = input(f"\n{Text.INPUT}[!]{Text.STANDARD} How many people will be playing with you? {Text.HINT}[Minimum 2 players | Maximum 10 Players | -1 to quit]{Text.STANDARD}\n")

        if num_players == "-1":
            time.sleep(0.5)
            print(Msgs.EXIT)
            break

        try:
            num_players = int(num_players)

            if num_players > 10:
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

def start_game():
    print(f"\n{Text.MESSAGE}[!]{Text.STANDARD}  Welcome to Python Yahtzee!  {Text.MESSAGE}[!]{Text.STANDARD}")
    time.sleep(0.5)

    num_players = get_num_players()

def main():
    start_game()

if __name__ == "__main__":
    main()
