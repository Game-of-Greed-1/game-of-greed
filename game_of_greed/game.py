from game_of_greed.game_logic import GameLogic
from game_of_greed.game_logic import Banker


class Game(GameLogic, Banker): 
    
    def play(self, roller=None):
        roller=roller or Game.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        decision = input("> ")

        if decision == "y":
            var1 = True
            round_num = 1
            dice_num = 6
            while var1:
                print(f"Starting round {round_num}")
                print(f"Rolling {dice_num} dice...")
                dice = roller(dice_num)
                sentence = "*** "
                for x in dice:
                    sentence = sentence + str(x) + " "
                sentence = sentence + "***"
                print(sentence)
                print("Enter dice to keep, or (q)uit:")
                dice_to_keep = input("> ") 
                if dice_to_keep == "q":
                    var1 = False
                    print(f"Thanks for playing. You earned {self.balance} points")
                else:
                    new_list = []
                    for x in dice_to_keep:
                        new_list.append(int(x))
                    tuple_list = tuple(new_list)
                    shelf_score = self.calculate_score(tuple_list)
                    self.shelf(shelf_score)
                    dice_num = dice_num - len(dice_to_keep) 
                    print(f"You have {self.shelved} unbanked points and {dice_num} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    decision2 = input("> ")
                    if decision2 == "r":
                        continue
                    elif decision2 == "b":
                        print(f"You banked {self.shelved} points in round {round_num}")
                        self.bank()
                        round_num += 1
                        print(f"Total score is {self.balance} points")
                        dice_num = 6
                    elif decision2 == "q":
                        print(f"Thanks for playing. You earned {self.balance} points")
                        var1 = False
        else: 
            print("OK. Maybe another time")

if __name__ == "__main__":
    game = Game()
    game.play()