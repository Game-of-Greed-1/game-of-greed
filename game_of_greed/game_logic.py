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

   
    def calculate_score(dice2):
        score=0
        dice=Counter(dice2)
        x=list(dice2)
        x.sort()
        if len(x)==6 and x[0]==1 and x[1]==2 and x[2]==3 and x[3]==4 and x[4]==5 and x[5]==6 :
            score=score+all_rules['Straight 1- 6']

        elif len(dice.most_common())==3 and dice.most_common()[1][1] == 2 and dice.most_common()[1][1] == 2 and dice.most_common()[2][1] == 2:
            score=score+all_rules['three pairs']

        else:
          for i in range(len(dice.most_common())):
              try:
                score=score+all_rules[(dice.most_common()[i][0]  ,dice.most_common()[i][1])]
              except KeyError:
                  score=score+0
        return score
        


    def roll_dice(times=6):
     return tuple(randint(1,6) for _ in range(0, times))
    #  return sample(range(1, 6 + 1), times)



 

if __name__ == "__main__":
    g = GameLogic
    d = g.roll_dice(6)
    print(d)
    result = g.calculate_score(d)
    print(result)


 