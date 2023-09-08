"""
Project to emphasize various concepts regarding string lists

By Solomon Stevens
Domain: Electric Cars
Date: September 8th, 2023

Uses random for random.choice function

"""

# imports first
import random

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)


# Define string lists
make = ['SUV', 'Car', 'Van', 'Truck', 'Car', 'Car', 'SUV']
type = ['Electric', 'Electric', 'Gasoline', 'Gasoline', 'Electric', 'Gasoline', 'Electric']
company = ['Toyota', 'Tesla', 'Honda', 'Chevrolet', 'Audi', 'Volkswagon', 'Ford']
haul = ['Passenger', 'Cargo']
location = ['city', 'suburbs', 'country']
road = ['city', 'backroads', 'highway']

# reusable functions next
# Define built_in_functions function
def built_in_functions():
    """Use length, set, and zip functions on lists of strings"""
    logger.info("")
    logger.info(f"===== Built In Functions =====")

    # len()
    len_make = len(make)
    len_type = len(type)
    len_company = len(company)
    len_haul = len(haul)
    len_location = len(location)
    len_road = len(road)

    #-> Log lengths
    logger.info(f"---< len() >---")
    logger.info(f"{len_make = }")
    logger.info(f"{len_type = }")
    logger.info(f"{len_company = }")
    logger.info(f"{len_haul = }")
    logger.info(f"{len_location = }")
    logger.info(f"{len_road = }")


    # set()
    unique_make = set(make)
    unique_type = set(type)
    unique_company = set(company)
    unique_haul = set(haul)
    unique_location = set(location)
    unique_road = set(road)

    #-> Log unique lists
    logger.info(f"---< set() >---")
    logger.info(f"{unique_make = }")
    logger.info(f"{unique_type = }")
    logger.info(f"{unique_company = }")
    logger.info(f"{unique_haul = }")
    logger.info(f"{unique_location = }")
    logger.info(f"{unique_road = }")


    #zip()
    make_and_type = zip(make, type)
    company_and_make = zip(company, make)
    company_make_type = zip(company, make, type)

    #-> Log zipped tuples
    logger.info(f"---< zip() >---")

    logger.info(f"=== Make and Type===")
    for i in range(len(make)-1):
        logger.info(f"Make: {make[i]:>5}    Type: {type[i]}")

    logger.info(f"=== Company and Make ===")
    for i in range(len(make)-1):
        logger.info(f"Company: {company[i]:>10}    Make: {make[i]}")
    
    logger.info(f"=== Company, Make and Type ===")
    for i in range(len(make)-1):
        logger.info(f"Company: {company[i]:>10}    Make: {make[i]:>5}    Type: {type[i]}")



# Define random_choice function
def random_choice():
    """Use random.choice to create randomly-generated sentences about cars"""
    logger.info("")
    logger.info(f"===== Random Choice =====")

    # Define local string lists
    comparisions = ['better', 'worse', 'higher', 'lower', 'more', 'less']
    descriptions = ['a little', 
                    'a bit', 
                    'much', 
                    'a WHOLE lot', 
                    'only the tiniest fraction']
    conclusions = ['Is that a bad thing?', 
                   'We should probabiy be careful', 
                   'Oh my!', 
                   '...meh, whatever.', 
                   'I did not know that.']
    #Create 3 separate sentences
    for i in [range(3)]:
        # Assign variables
        make1 = random.choice(make)
        make2 = random.choice(make)

        #-> if the same, reassign make2
        while make1 == make2:
            make2 = random.choice(make)


        type1 = random.choice(type)
        type2 = random.choice(type)
        #-> It doesn't matter if the types are the same


        company1 = random.choice(company)
        company2 = random.choice(company)

        #-> if the same, reassign company2
        while company1 == company2:
            company2 = random.choice(company2)
            

        # Create and Log random sentences
        logger.info(f"{type1} {company1} {make1}s have {random.choice(descriptions)} {random.choice(comparisions)} than {type2} {company2} {make2}s do. {random.choice(conclusions)}")

#Define get_unique_words function
def get_unique_words():
    """Count the number of times each word is in a certain text file"""
    logger.info("")
    logger.info(f"===== Get Unique Words in a Text File =====")

    # Get file to read and split words
    file_to_open = "text_hamlet.txt"
    with open(file_to_open, "r") as txtFile:
        text = txtFile.read()
        words = text.split()
        unique_words = set(words)

    # Sort the list
    sorted_text = sorted(text)

    # Get the counts of each
    count_text = len(sorted_text)
    count_text_unique = len(unique_words)

    # Log findings
    logger.info(f"File selected: {file_to_open}")
    logger.info(f"For the sake of sanity, I have chosen not to display the file... it's long.")
    logger.info(f"Number of words: {count_text}")
    logger.info(f"Number of distinct words (no duplicates): {count_text_unique}")



# call functions and execute code
# use if __name__ == "__main__":

if __name__ == "__main__":
    # Call functions
    built_in_functions()
    random_choice()
    get_unique_words()

