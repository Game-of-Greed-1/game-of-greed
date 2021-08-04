from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
import sys

class Game(GameLogic, Banker): 
    
    def __init__(self, num_rounds=5):
        self.banker = Banker()
        self.num_rounds = num_rounds

    def play(self, roller=None):
        """Entry point for playing (or declining) a game
        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """
        self.num_rounds += 1
        self.round = 0
        self.remaining_dice = 6
        self._roller = roller or GameLogic.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        response = input("> ")
        if response == "y" or response == "yes":
            self.play_here()
        else:
            self.quit()

    def quit(self):
        print("OK. Maybe another time")

    def thank_for_playing(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()

    def shelf_dice(self, dice_choice):   
        score = GameLogic.calculate_score(dice_choice)
        self.banker.shelf(score)
        shelved = self.banker.shelved
        self.remaining_dice_count -= len(dice_choice)
        print(f"You have {shelved} unbanked points and {self.remaining_dice_count} dice remaining")

    def roll_the_dice(self):
        print(f"Rolling {self.remaining_dice_count} dice...")
        roll = self._roller(self.remaining_dice_count)
        self.print_roll(roll)
        return roll

    def zilch(self):
        print(  
            
"""****************************************
**        Zilch!!! Round over         **
****************************************""")

        self.banker.clear_shelf()
        self.bank_points()


    def print_roll(self, roll):
        re_roll = ' '.join(map(str, (roll)))
        print(f"*** {re_roll} ***")

    def bank_points(self):
        round_score = self.banker.shelved
        self.banker.bank()
        print(f"You banked {round_score} points in round {self.round}")
        print(f"Total score is {self.banker.balance} points")

    def input_to_tuple(self, input):
        dice_choice = []
        for characters in input:
            if characters != ' ':
                dice_choice.append(int(characters))
        return tuple(dice_choice)

    def new_round(self):
        self.remaining_dice_count = self.remaining_dice 
        roll = self.roll_the_dice()
        print('Enter dice to keep, or (q)uit:')
        user_input = input("> ")
        while user_input != "q" or self.num_rounds == self.round:  
            tuple_die = self.input_to_tuple(user_input)
            if not GameLogic.validate_keepers(roll, tuple_die): 
                print("Cheater!!! Or possibly made a typo...")
                self.print_roll(roll)
                print('Enter dice to keep, or (q)uit:')
                user_input = input("> ")
            else:   
                self.shelf_dice(tuple_die)
                print('(r)oll again, (b)ank your points or (q)uit:')
                bank_choice = input("> ")
                if bank_choice == "q" or bank_choice == "quit" or self.num_rounds == self.round +1:
                    self.thank_for_playing() 
                if bank_choice == "r" or bank_choice == "roll":
                    if self.remaining_dice_count == 0:
                        self.remaining_dice_count = 6
                    roll = self.roll_the_dice()
                    if GameLogic.calculate_score(roll) == 0:
                        self.zilch()
                        return
                    print('Enter dice to keep, or (q)uit:')    
                    user_input = input("> ")
                if bank_choice == "b" or bank_choice == "bank":
                    self.bank_points()
                    return
        self.thank_for_playing()
        
    def play_here(self):
        for i in range(1, self.num_rounds):
            self.round += 1
            print(f"Starting round {self.round}")
            self.new_round()


if __name__ == "__main__":
    new_game = Game()
    new_game.play()