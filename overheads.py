
from pathlib import Path
import csv

# create a file to csv file
fp = Path.cwd()/"csv_report"/"overheads.csv"

# read the csv file to append category and overhead from the csv
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list to store category and overhead
    overheads = []

    # append category and overhead into the overheads list
    for row in reader:
        # get the category and overhead (percentage) for day 90 record 
        # and append the overheads list
        # convert type for overhead from integer to float
        overheads.append([row[0],float(row[1])])


def identifying_highest_overhead(overheads):
    """
    - This function will identify the highest overhead 
    - Parameter required: overheads  
    """
    
    # create a variable attached with a number of type 'float'
    highest_overhead = 0.0
    highest_category = ()

    # iterating through the datas in overheads list to find out which is the highest overhead 
    # and find the category of it
    for category, overhead in overheads:
        if overhead > highest_overhead:
            highest_overhead = overhead
            highest_category = category

    return highest_category, highest_overhead