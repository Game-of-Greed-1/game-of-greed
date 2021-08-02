class Game:
    def __init__(self, roller=None):
        self.roller = roller
    # @staticmethod
    # def print_roll(roll):
    #     print(','.join([str(i) for i in roll]))
    def play(self):
        print('Welcome to Game of Greed')
        res = input('Wanna play?')
        if res == 'n':
            print('OK. Maybe another time')
        elif res == 'y':
            round = 1
            remaining_dice = 6
            score = 0
            banked = 0
            print(f'Starting round {round}')
            print(f'Rolling {remaining_dice} dice...')
            roll = self.roller(remaining_dice)
            # Game.print_roll(roll)
            print(','.join([str(i) for i in roll]))
            dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')
            if dice_to_keep == 'q':
                print(f'Total score is {score} points')
                print(f'Thanks for playing. You earned {score} points')
            else:
                if dice_to_keep == '5':
                    banked = 50
                if dice_to_keep == '1':
                    banked = 100
                print(f"You have {banked} unbanked points and 5 dice remaining")
                bank = input ("(r)oll again, (b)ank your points or (q)uit ")
                if bank == 'b':
                    print(f"You banked {banked} points in round {round}")
                    score += banked
                    print(f"Total score is {score} points")
                    round += 1
                    print (f"Starting round {round}")
                    print (f"Rolling {remaining_dice} dice...")
                    roll = self.roller(remaining_dice)
                    print(','.join([str(i) for i in roll]))
                    dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')
                    if dice_to_keep == 'q':
                        print(f"Total score is {score} points")
                        print(f'Thanks for playing. You earned {score} points')
                    elif dice_to_keep == '1':
                        print(f"You have {banked} unbanked points and 5 dice remaining")
                        bank = input ("(r)oll again, (b)ank your points or (q)uit ")
                        if bank == 'b':
                            print(f"You banked {banked} points in round {round}")
                            score += banked
                            print(f"Total score is {score} points")
                            round += 1
                            print (f"Starting round {round}")
                            print (f"Rolling {remaining_dice} dice...")
                            roll = self.roller(remaining_dice)
                            print(','.join([str(i) for i in roll]))
                            dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')
                            if dice_to_keep == 'q':
                                print(f"Total score is {score} points")
                                print(f'Thanks for playing. You earned {score} points')
if __name__ == '__main__':
    pass