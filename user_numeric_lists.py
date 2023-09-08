"""
Program to create and statistically analyze lists

By Solomon Stevens
Domain: Electric Cars
Date: September 8th, 2023

Uses "math" module for mathematical functions
Uses "random" to get list of random numbers
Uses "statistics" for measures of central tendancy / difference
"""

# Import some standard modules first - how many can you make use of?
import math
import random
import statistics

# Import logger
from util_datafun_logger import setup_logger            #-> Import from local util_datafun_logger.py
logger, logname = setup_logger(__file__)                #-> Call the setup_logger function to create a logger and get the log file name
                                                        #--> 2 underscores before and after "file"

# Create some shared data lists if you like - or just create them in your functions
#-> Create empty list
list1 = []

#-> Fill empty list with random numbers
for i in range(25):
    list1.append(random.randrange(10,31))


#-> Create x list
listx = range(10)


#-> Create y list
#--> Create empty list
listy_dummy = []

#--> Fill in list with sorted random numbers
for i in range(10):
    listy_dummy.append(random.randrange(150,400))

#--> Sort list and store in listy
listy = sorted(listy_dummy)                             # listy should now have some sort of correlation with list x since they are in order


#Log lists
logger.info(f"===== Lists =====")
logger.info(f"{list1 = }")
logger.info(f"{listx = }")
logger.info(f"{listy = }")

# Define basic_univariate_measures function
def basic_univariate_measures():
    """Calculate basic statistical measures of a list"""

    logger.info("")
    logger.info(f"===== Basic Measures of Central Tendancy and Difference =====")

    # List basic measures of list1
    mean = statistics.mean(list1)
    med = statistics.median(list1)
    mode = statistics.mode(list1)
    var = statistics.variance(list1)
    stdev = statistics.stdev(list1)

    # Log basic measures
    logger.info(f"{mean = }")
    logger.info(f"{med = }")
    logger.info(f"{mode = }")
    logger.info(f"{var = }")
    logger.info(f"{stdev = }")


# Define correlate_and_predict function
def correlate_and_predict():
    """Calculate the correlation of two lists and predict what a value could be in the future"""

    logger.info("")
    logger.info(f"===== Correlation and Prediction for Bivariate Data =====")

    # List and Log correlation between listx and listy
    correl = statistics.correlation(listx, listy)
    logger.info(f"The correlation between listx and listy = {correl}.")

    # Make a prediction for a future x value
    #-> Find the linear relation (slope and intercept)
    slope, intercept = statistics.linear_regression(listx, listy)

    #-> Use this information to calculate the y value when x wold be 15
    predictx = 15
    predicty = (slope * predictx) + intercept

    # Log prediction
    logger.info(f"When x = {predictx}, y should be approximately {predicty}.")


# Define basic_list_statistics function
def basic_list_statistics():
    """Perform built-in functions on a list of numbers"""

    logger.info("")
    logger.info(f"===== Basic Univariate Statistical Operations =====")

    # Calculate basic statistical operations on list1
    lowest = min(list1)
    highest = max(list1)
    count = len(list1)
    total = sum(list1)
    avg = total / count
    unique_values = set(list1)
    low_to_high = sorted(list1)
    high_to_low = sorted(list1, reverse=True)

    # Log findings
    logger.info(f"{lowest = }")
    logger.info(f"{highest = }")
    logger.info(f"{count = }")
    logger.info(f"{total = }")
    logger.info(f"{avg = }")
    logger.info(f"{unique_values = }")
    logger.info(f"{low_to_high = }")
    logger.info(f"{high_to_low = }")



# Define list_methods function
def list_methods():
    """Practice various list methods on a random list"""

    logger.info("")
    logger.info(f"===== List Methods =====")

    # Create local list to work with
    #-> Create empty list
    list_local = []

    #-> Fill in list with random numbers
    for i in range(10):
        list_local.append(random.randrange(1,9))
    
    # Log beginning list
    logger.info(f"Beginning list: {list_local}")


    # Append random number to end of list and Log changes
    list_local.append(random.randrange(1,9))
    logger.info(f"List after appending: {list_local}")


    # Extend list with another list and Log changes
    #-> Create new list to extend onto original list
    #--> Create empty list
    list_extension = []

    #--> Fill in list
    for i in range(3):
        list_extension.append(random.randrange(1,9))

    #-> Extend new list onto original
    list_local.extend(list_extension)

    #-> Log new list
    logger.info(f"List after extending: {list_local}")


    # Insert a random number to a random index and Log changes
    #-> Randomly select index
    index = random.randrange(0,len(list_local)-1)

    #-> Randomly select number
    number = random.randrange(1,9)

    #-> Insert new number at index
    list_local.insert(index, number)

    #-> Log new list
    logger.info(f"List after inserting {number} at index {index}: {list_local}")


    # Remove a 5 from the list and Log changes
    #-> Make sure we have a 5 to avoid a ValueError
    #--> Pick an index at random
    index = random.randrange(0,len(list_local)-1)

    #--> Insert a 5 at that index
    list_local.insert(index, 5)

    #-> Remove first instance of 5
    list_local.remove(5)

    #-> Log new list
    logger.info(f"List after removing first 5: {list_local}")


    # Count how many times the number 2 appears
    num_of_2s = list_local.count(2)

    #-> if zero, make a random number a 2
    if num_of_2s == 0:
        #--> Pick a random index
        index = random.randrange(0,len(list_local)-1)

        #--> Insert a 2 at that index
        list_local.insert(index, 2)

        #--> Recount the number of 2s.  Should be 1
        num_of_2s = list_local.count(2)

    # Log new list
    logger.info(f"Number of 2s: {num_of_2s}")


    # Sort list forwards and backwards and Log changes
    #-> Forwards
    list_local.sort()
    logger.info(f"List after sorting forwards (L to H): {list_local}")

    #-> Backwards
    list_local.sort(reverse = True)
    logger.info(f"List after sorting backwards (H to L): {list_local}")


    # Copy list and Log copied list
    list_copied = list_local.copy()
    logger.info(f"Original list: {list_local}")
    logger.info(f"Copied list: {list_copied}")


    # Pop first and last items off list and Log changes
    #-> Pop first item off list
    pop_first = list_local.pop(0)
    logger.info(f"List after popping {pop_first} from beginning of list: {list_local}")

    #-> Pop last item off list
    pop_last = list_local.pop(-1)
    logger.info(f"List after popping {pop_last} from end of list: {list_local}")


# Define filter_and_map function
def filter_and_map():
    """Use filter() and map() to find / calculate values based on a given list"""

    logger.info("")
    logger.info(f"===== Filter and Map =====")

    # Filter numbers out of list1 and Log changes
    x_greater_than_14 = list(filter(lambda x: (x < 14), list1))
    x_even = list(filter(lambda x: (x % 2 == 0), list1))
    logger.info(f"List of values greater than 14 in list1: {x_greater_than_14}")
    logger.info(f"List of even values in list1: {x_even}")

    # Map each x to it's cube root and Log changes
    x_cube_root = list(map(lambda x: (math.pow(x, 1/3)), list1))
    logger.info(f"List of cube roots of all numbers in list1: {x_cube_root}")

    # Map each x to volume of cube that has the side of length x... (basically just cube x) and Log changes
    x_volume_cube = list(map(lambda x: (x ** 3), list1))
    logger.info(f"The volume of a cube with side lengths of each value in list1: {x_volume_cube}")

    #NOTE: Had to use list() rather than [] to make it work. Not sure why.


# Define list_comprehension function
def list_comprehension():
    """Practice the format of list comprehension"""

    logger.info("")
    logger.info(f"===== List Comprehentions =====")

    # Find all values in list1 less than 14 and Log output
    get_x_less_than_14 = [x for x in list1 if x < 14]
    logger.info(f"Numbers less than 14: {get_x_less_than_14}")

    # Triple each value in list1 and Log output
    tripled_x = [3*x for x in list1]
    logger.info(f"List times 3: {tripled_x}")

    # Find out how far each number in list1 is away from a random number in the list and Log findings
    #-> Randomly select number
    rand_number = random.randrange(min(list1), max(list1))

    #-> Calculate difference for each number in list1
    away_from = [abs(x - rand_number) for x in list1]

    #-> Log findings
    logger.info(f"Here is how far each number in list1 is away from {rand_number}: {away_from}")


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # Call your functions here (see instructions)
    basic_univariate_measures()
    correlate_and_predict()
    basic_list_statistics()
    list_methods()
    filter_and_map()
    list_comprehension()


