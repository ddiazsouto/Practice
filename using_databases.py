
"""
    You will need to install pymysql for this
    ---
    from the consle:
        pip install pymysql

    You do that once nad that is it forever
"""
import pymysql      # import module before using it in every program



# leave host and user like this, also db unless using specific database

Make = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = 'Passwordhere', db='database')
MySQL = Make.cursor()   # This just copy and paste

# Make and MySQL are my choice, you can name them whatever you want




"""
    Random numbers and brief use of data structures
"""

from random import randint  

random_number = randint(1, 100)    # this creates a random number

random_list = list(randint(1, 99) for i in range(100)) # this creates a list of random numbers


# We are going to create now a list with names, so is not all numbers

names = ['Wesley', 'Julian', 'Chris', 'Daniel', 'Misterious man X']


# We can assign a list of numbers to each person, we can use dictionaries for that

my_dictionary ={'Wesley':125, 'Daniel':143} # Just a useless example


# Now something useful, we can mix it up and have a dictionary with a list per name
# Here pause and ponder, why can we not assign more than one number to each name
# in the dictionary?? That is why we need to use lists - Google that

useful_dict = {'Wesley':[], 'Julian':[], 'Chris':[], 'Daniel':[]}



"""
        Please don't try to understand this function
        I just want to give some format to the (random) data

        --- 
        I am trying to create a dictionary of names where each name 
        'owns' a list of numbers, random numbers of course, there is no 
        particular pattern to what I am doing, but this data 
        could be used for posterior analysis
"""

def Parsing(list_of_random_numbers: list, useful_dict: dict):
    
    for each_number in list_of_random_numbers:

        randomize1 = randint(1, 4)
        randomize2 = randint(1, 4)

        randomize = (randomize1*randomize2)//2

        if randomize == 1:
            useful_dict['Wesley'].append(each_number)
        elif randomize == 2:
            useful_dict['Julian'].append(each_number)
        elif randomize == 2:
            useful_dict['Chris'].append(each_number)
        elif randomize == 2:
            useful_dict['Daniel'].append(each_number)

    return useful_dict


"""
                         OK NOW SQL
    ---
    I will create the SQL statements in strings, 
    then pass the variable to the pymysql function.

    Simply to increase readability

"""

# We already created Make and MySQL but we highlight it again
# Make = pymysql.connect()
# MySQL = Make.cursor() 


#  In general pymysql works like this:

MySQL.execute(" SHOW DATABASES; ") # Where SHOW DATABASES is SQL code

# Basic SQL commands are INSERT to input data and SELECT to get data, i.e.

command  =  " CREATE DATABASE Practice;"
MySQL.execute(command)

