from random import randint, sample, random
from collections import Counter
from tests.flo import *

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