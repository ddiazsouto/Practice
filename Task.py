# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 09:18:17 2021

@author: DestRuktoR
"""

from random import randint

random_number = randint(1, 50)

my_list = []

for iteration in range(1, 100):
    
    my_list.append(randint(1, 10))
    
    

""" 
    Ceate a function that emulates the toss of a coin
"""

def toss(number_of_times):
    """
        The function will take the number of times we toss the coin.
        
        it will return a list with the result
        
        Input example:
            toss(3)
        
        Output example:
            result = ['Heads', 'Heads', 'Tails']

    """
    
    options = ['Heads', 'Tails']
    




"""
    Can you use this function to insert data in a database with 200 rows?
"""