import collections
from itertools import count
from random import randint, sample, random

class GameLogic():
    

    def __init__(self):
        pass 
    
    def calculate_score(test_input):
        score = 0
        pairs =0 
        num = (collections.Counter(test_input))
        
        if num == None:
            return 0


        if 1 in num and 2 in num and 3 in num and 4 in num and 5 in num and 6 in num:
            
            score+=1500
            return score
        
        if (num[1] == 1) and 5 in num:
            score+=150
            return score

        if (num[1] == 3) and 5 in num:
            score+=1050
            return score

        for i in num:
            

            if num[i] == 2:
                pairs = pairs + 1 
                if pairs == 3 :
                    score = 0
                    score = score +1500
                    return score
            
            if i == 5 and num[i] < 3:
                score = score + (num[i]*50)
                return score


            if i == 1 and num[i] < 3:
                score = score + (num[i]*100)
                return score
             
            if num[i] >= 3 and i == 1:
                score = score + 1000
                num[i] = num[i] - 3
                for i in range (num[i]):
                    score = score + 1000
                    continue
            
            if num[i] == 3   and i != 1:
                score = score + (i*100)
                num[i] = num[i] - 3
                for i in range (num[i]):
                    score = score + 100
                    continue
            
            if num[i] > 3   and i != 1:
                score = score + ((num[i]-2)*i*100)
                return score
                continue
        return score

    def roll_dice(times=6):
        return tuple(randint(1,6) for _ in range(0, times))
    #  return sample(range(1, 6 + 1), times)


if __name__ == "__main__":
    new_game = GameLogic()

    print(new_game)
