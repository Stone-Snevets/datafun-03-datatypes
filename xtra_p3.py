"""
Program to explore "corpus" text files and find similarities

Modified by Solomon Stevens
Date: September 8th, 2023

Optional bonus. See course site for details.

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest

# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)


def compare_two_plays():
    ''' This function compares two plays by Shakespeare.'''
    logger.info("Calling compare_two_plays()")
        
    # read from file and get a list of words

    with open("text_hamlet.txt", "r") as f1:
        text = f1.read()
        wordlist1 = text.split()  # split on whitespace

    #--------logger.info(f"List of words from play 1: {wordlist1}")


    # read from file and get a list of words

    with open("text_juliuscaesar.txt", "r") as f2:
        text = f2.read()
        wordlist2 = text.split()  # split on whitespace

    #---------logger.info(f"List of words from play 2: {wordlist2}")


    # Done with files - let the files close and the work begin

    # Remove duplicates by creating two sorted sets
    # hint: use sorted() to sort the list
    # hint: use set() to remove duplicates
    # name them wordset1 and wordset2
    wordset1 = set(sorted(wordlist1))
    wordset2 = set(sorted(wordlist2))


    #-> Logging current findings
    logger.info("")
    logger.info(f"Number of words in text_hamlet.txt: {len(wordlist1)}")
    logger.info(f"Number of unique words in text_hamlet.txt: {len(wordset1)}")
    logger.info(f"Number of words in text_juliuscaesar.txt: {len(wordlist2)}")
    logger.info(f"Number of unique words in text_juliuscaesar.txt: {len(wordset2)}")


    # initialize a variable maxlen = 10
    maxlen = 10

    # use a list comprension to get a list of words longer than 10
    # for word in wordset1
    # That is:
    # in a list (e.g. square brackets)
    # say "[Give me word (for each word in wordset1)
    #      if len(word) is greater than maxlen]"
    # then convert the list to a set to we can take the intersection
    # hint: use set()
    # name them longwordset1 and longwordset2

    longwordset1 = set([word for word in wordset1 if len(word) > maxlen])
    longwordset2 = set([word for word in wordset2 if len(word) > maxlen])

    # find the intersection of the two sets
    # that is, the words in both longwordset1 1 & longwordset2
    # name this variable longwords
    longwords = longwordset1 & longwordset2

    # print the length of the sets and the list
    #-> print() doesn't want to work for some reason.  Not sure why.
    #-----------------------------------------
    #print(len(longwordset1))
    #print(len(longwordset2))
    #print(len(longwords))
    #print()
    #print(f"{sorted(longwords) = }")
    #print()
    #----------------------------------------
    logger.info("")
    logger.info(f"{len(longwordset1) = }")
    logger.info(f"{len(longwordset2) = }")
    logger.info(f"{len(longwords) = }")
    logger.info("")
    logger.info(f"{sorted(longwords)}")

    # check your work
    print("TESTING...if nothing prints before the testing is done, you passed!")
    doctest.testmod()
    print("TESTING DONE")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    compare_two_plays()

    logger.info("Complete the code to compare two plays.")
    show_log()

