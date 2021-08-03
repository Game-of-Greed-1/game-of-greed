from random import randint, sample, random
from collections import Counter
from tests.flo import *


def __init__(self):
        pass 

    
roles = {   
    (1,1):100, (5,1):50, (1,3):1000, (1,4):2000,
    (1,5):3000, (1,6):4000, (2,3):200, (2,4):400,
    (2,5):600, (2,6):800, (3,3):300, (3,4):600,
    (3,5):900, (3,6):1200, (4,3):400, (4,4):800, 
    (4,5):1200, (4,6):1600, (6,6):2400, (6,5):1800,
    (6,4):1200, (6,3):600, (5,6):2000, (5,5):1500,
    (5,4):1000, (5,3):500, (1,2):200, (2,2):0,
    (3,2):0, (4,2):0, (5,2):100,(6,2):0, 
    (2,1):0, (3,1):0, (4,1):0, (6,1):0,
    }

class GameLogic:

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


class Banker:

    def __init__(self):
        self.shelved = 0
        self.balance= 0
 
    def shelf(self,num):
        self.shelved += num
   
    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    def clear_shelf(self):
        self.shelved = 0
    




if __name__ == "__main__":
    new_game = Game()
    new_game.play()