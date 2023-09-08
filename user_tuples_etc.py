"""
Program to practice the uses and functions of tuples

Written by Solomon Stevens
Domain: Electric Cars
Date: September 8th, 2023

Uses random for random tuple generation

"""

# Imports
#-> Import modules
import random

#-> Import Logger
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)


# Create global tuples
#-> Create empty tuples
tup1 = (random.randrange(25,35) for x in range(10))     # Replicate the wheel diameter of a car in inches
tup2 = (random.randrange(3,10) for x in range(10))      # Replicate the number of "unnecessary" features in a car that may waste battery life

# Log tuples
logger.info("===== Tuples Randomly Generated =====")
logger.info(f"{tup1 = }")
logger.info(f"{tup2 = }")


# Define working_with_sets function
def working_with_sets():
    """Create two sets and find their union and intersection"""

    logger.info("")
    logger.info("===== Working with Sets =====")

    # Create two sets of random numbers
    set1 = {random.randrange(1,150) for x in range(10)}
    set2 = {random.randrange(100,400) for x in range(10)}

    # Get union and intersection
    set_union = set1 | set2
    set_intersection = set1 & set2

    # Log sets, union, and intersection
    logger.info(f"{set1 = }")
    logger.info(f"{set2 = }")
    logger.info(f"{set_union = }")
    logger.info(f"{set_intersection = }")


# Define working_with_dictionaries function
def working_with_dictionaries():
    """Use Dictionaries to collect and count words from a file"""

    logger.info("")
    logger.info("===== Working with Dictionaries =====")


    # Open file to read
    file_to_read = "text_zen_of_python.txt"
    with open(file_to_read) as fileObject:
        list_of_words = (fileObject.read()).split()

    # Create a dictionary key-value for each word
    dictionary_of_words = {word: list_of_words.count(word) for word in list_of_words}

    # Log outputs
    logger.info(f"File Chosen: {file_to_read}")
    logger.info(f"{dictionary_of_words = }")



# Define MAIN function
if __name__ == "__main__":
    """Call user-created functions"""

    working_with_sets()
    working_with_dictionaries()