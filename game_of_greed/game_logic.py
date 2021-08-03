from random import randint, sample, random
from collections import Counter
from tests.flo import *




    
roles = {   
    (1,1):100, (5,1):50, (1,3):1000, (1,4):2000,
    (1,5):3000, (1,6):4000, (2,3):200, (2,4):400,
    (2,5):600, (2,6):800, (3,3):300, (3,4):600,
    (3,5):900, (3,6):1200, (4,3):400, (4,4):800, 
    (4,5):1200, (4,6):1600, (6,6):2400, (6,5):1800,
    (6,4):1200, (6,3):600, (5,6):2000, (5,5):1500,
    (5,4):1000, (5,3):500, (1,2):200, (2,2):0,
    (3,2):0,    (4,2):0, (5,2):100,(6,2):0, 
    (2,1):0, (  3,1):0, (4,1):0, (6,1):0,
    }

class GameLogic:

    def __init__(self, currnt_round = 0):
        self.current_round = currnt_round

    @staticmethod
    def calculate_score(test_input:tuple) -> int:
        score = 0
        num = Counter(test_input).most_common()
        stright = sorted(test_input)
        
        if stright == [1,2,3,4,5,6]:
            score = 1500
            return score
        elif len(num) == 3 and num[2][1] == 2:
            score = 1500
            return score

        for x in num:
            score += roles[x]
        return score
    
    
    def roll_dice(times=6):
        return tuple(randint(1,6) for _ in range(0, times))
    #  return sample(range(1, 6 + 1), times)
    
    @staticmethod
    def validate_keepers(roll:tuple, keepers:tuple) -> int:
        roll = list(roll)
        for dieces in keepers:
            if dieces not in roll:
                return False
            roll.remove(dieces) 
        return True

    def get_scorers(all_dice :tuple) -> int():     
        all_score = GameLogic.calculate_score(all_dice)
        scorers = []
        if all_score:
            for i in range(len(all_dice)):
                greed_roll = all_dice[:i] + all_dice[i + 1:]
                greed_score = GameLogic.calculate_score(greed_roll)
                if greed_score != all_score:
                    scorers.append(all_dice[i])

        return tuple(scorers)
    

if __name__ == "__main__":
    new_game = Game()
    new_game.play()