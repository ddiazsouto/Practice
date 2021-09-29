
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

b = list(randint(1, 99) for i in range(100)) # this creates a list of random numbers