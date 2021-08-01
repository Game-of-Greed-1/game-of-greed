from collections import Counter
from itertools import count
from random import randint, sample, random

all_rules = {  
        "Straight 1- 6": 1500,
        "Three Pairs": 1500,
        '(1, 1)': 100, 
        '(1, 2)': 200, 
        '(1, 3)': 1000,  
        '(1, 4)': 2000,  
        '(1, 5)': 3000, 
        '(1, 6)': 4000,  
        '(2, 3)': 200,  
        '(2, 4)': 400,   
        '(2, 5)': 600,  
        '(2, 6)': 800, 
        '(3, 3)': 300, 
        '(3, 4)': 600,  
        '(3, 5)': 900,  
        '(3, 6)': 1200,  
        '(4, 3)': 400,  
        '(4, 4)': 800,  
        '(4, 5)': 1200, 
        '(4, 6)': 1600,  
        '(5, 1)': 50,  
        '(5, 2)': 100,  
        '(5, 3)': 500,  
        '(5, 4)': 1000,  
        '(5, 5)': 1500,  
        '(5, 6)': 2000,  
        '(6, 3)': 600,   
        '(6, 4)': 1200,  
        '(6, 5)': 1800,  
        '(6, 6)': 2400,}

class GameLogic:

    @staticmethod
    def calculate_score(dice_roll):
   
        sum=0
        ctr = Counter(dice_roll)
        if len(dice_roll) == 0:
            return 0
        if ctr.most_common(1)[0][1] == 1 and len(ctr.most_common()) == 6:
            print(len(ctr.most_common()))
            return 1500
        if ctr.most_common(1)[0][1] == 2 and ctr.most_common(2)[0][1] == 2 and ctr.most_common(3)[0][1] == 2 and len(ctr.most_common()) == 3:
            return 1500
        for i in ctr.most_common():
            sum = sum + all_rules[f'{i}']
        
       
        return sum
         
    
    def roll_dice(times=6):
     return tuple(randint(1,6) for _ in range(0, times))
    #  return sample(range(1, 6 + 1), times)



 

if __name__ == "__main__":
    g = GameLogic
    

 