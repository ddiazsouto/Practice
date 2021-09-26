

# -*- coding: utf-8 -*-
"""
            LISTS


"""



empty_list = []
list1 = [1,2,3,4,5,6,7,8,9]

#also known as:
list_1 = [each for each in range(1,10)]    # list1 == list_1

"""
    Lists are cool because they maintain their order:
        a = [1,2,3] is not the same as b = [3,2,1]
    
    so when you iterate a you get: 1 2 3
    and when iterate b you get 3 2 1
    
    
The main thing to do with it is the function append() 
which adds something to the end of the list
"""

empty_list.append(1)

#also:
some_variable = 2

empty_list.append(some_variable)
# You can see how this latter way can be very useful with more complex code


"""
The opposite function would be to remove something from the end,
you do it with pop()
pop() returns the last value of the list

You may know that by now the list looks like this:
    empty_list = [1,2]

"""

empty_list.pop()      # This returns 2

#also

other_variable = empty_list.pop()

# Lists can be integers, strings, boolean and so on

real_list = [True, 2, 5, 7, 'Wesley', other_variable, False]

# THAT'S IT, should be enough to play around with lists now.

"""
Task 1

    CREATE A PROGRAM THAT ITERATES THE LIST real_list WITH A FOR LOOP 
    AND PRINTS YOUR NAME WHEN IT FINDS IT
    
    ---
    Research and expand, (use Google)
    print also the position that element takes in the list

"""
for i in real_list:     # Kind of like this
    print(i)
    

"""
Task 2 

    USE THE any_variable = input() FUNCTION TO CREATE A PROGRAM THAT ASKS YOU
    TO INPUT A NUMBER THREE TIMES AND THEN IT RETURNS A LIST WITH THE INPUT
    
    ---
    Expand, create a function that takes the list below, 
    when the function runs the algorithm should keep asking you to type an input
    and then it prints ' Correct' when the input is 'Lum'
    
    
    Note that input is stored as a sting by default
    
"""

Changed_var = [False, 'Lum', True]
