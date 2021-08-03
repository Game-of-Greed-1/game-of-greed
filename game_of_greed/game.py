from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game(GameLogic, Banker): 
    
    def play(self, roller = None):
        roller = roller or Game.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        choice = input("> ")

        if choice == "y":
            input_choies = True
            round = 1
            remaining_dice = 6
            while input_choies:
                print(f"Starting round {round}")
                print(f"Rolling {remaining_dice} dice...")
                dice = roller(remaining_dice)
                start_sentence = "*** "
                for x in dice:
                    start_sentence = start_sentence + str(x) + " "
                start_sentence = start_sentence + "***"
                print(start_sentence)
                print("Enter dice to keep, or (q)uit:")
                dice_to_keep = input("> ") 
                if dice_to_keep == "q":
                    input_choies = False
                    print(f"Thanks for playing. You earned {self.balance} points")
                else:
                    remaining = []
                    for x in dice_to_keep:
                        remaining.append(int(x))
                    new_list = tuple(remaining)
                    shelf_score = self.calculate_score(new_list)
                    self.shelf(shelf_score)
                    remaining_dice = remaining_dice - len(dice_to_keep) 
                    print(f"You have {self.shelved} unbanked points and {remaining_dice} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    choice2 = input("> ")
                    if choice2 == "r":
                        continue
                    elif choice2 == "b":
                        print(f"You banked {self.shelved} points in round {round}")
                        self.bank()
                        round += 1
                        print(f"Total score is {self.balance} points")
                        remaining_dice = 6
                    elif choice2 == "q":
                        print(f"Thanks for playing. You earned {self.balance} points")
                        input_choies = False
        else: 
            print("OK. Maybe another time")

if __name__ == "__main__":
    new_game = Game()
    new_game.play()