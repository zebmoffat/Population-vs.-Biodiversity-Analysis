__author__ = "Zeb Moffat"
__date__ = "10/22/2024"

import pandas as pd
import openpyxl as xl
import pickle
import csv
import time

def process_data(bio_path, pop_path, clean_bio_name, clean_pop_name):
    bio_dict = process_bio_data(bio_path)
    write_bio_data(clean_bio_name, bio_dict)
    pop_dict = process_pop_data(pop_path)
    write_pop_data(clean_pop_name, pop_dict)

def process_bio_data(bio_path):
    print("\tReading and processing population data from " + bio_path)
    time.sleep(0.5)
    cleaned_dictionary = dict()

    with open(bio_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        #Iterator to skip over first row of field names
        i = 0

        # Iterate over each row in the CSV
        for row in csv_reader:
            if i > 0:

                #There are three rows in the dataset from unknown counties with extirpated distribution statuses.
                #Since they are only 3 of our 20507 rows, skip them as they cannot be assigned to a county and make
                #up such a small amount of the data.
                if row[0] == "Counties Unknown":
                    continue

                #There are fourteen rows in the dataset from the "Atlantic Ocean and Long Island Sound". Since these
                #are not New York counties, we need to remove them from our cleaned data.
                elif row[0] == "Atlantic Ocean and Long Island Sound":
                    continue

                #There are 4 rows for "Lake Ontario Open Waters" and 1 row for "Lake Erie Open Waters". Since these
                #are not New York counties, we need to remove them from our cleaned data.
                elif row[0] == "Lake Ontario Open Waters" or row[0] == "Lake Erie Open Waters":
                    continue

                #If this county is not present as a key within the dictionary, add it
                elif row[0] not in cleaned_dictionary.keys():
                    cleaned_dictionary[row[0]] = list()

                #If a range is given in the year last documented, e.g. 1990-1999, use the most recent year for
                #better accuracy to now
                if "-" in row[6]:
                    row[6] = row[6].split("-")[1]

                #If no year is given for last year documented,
                #replace with a 0 so those rows can easily be seperated if needed
                elif "not available" in row[6]:
                    row[6] = "0"

                #Cast all years to integer
                row[6] = int(row[6])

                #Add the group being measured as the value to its county within the dictionary
                cleaned_dictionary[row[0]].append(row[1:])

            #Skip first row
            else:
                i += 1

    return cleaned_dictionary

def process_pop_data(pop_path):
    print("\tReading and processing population data from " + pop_path)
    time.sleep(0.5)
    #Usw pandas and openpyxl to read in the data as an xlsx file.
    unclean = pd.read_excel(pop_path, skiprows=4, skipfooter=6, engine='openpyxl')

    cleaned_dictionary = dict()

    for index, row in unclean.iterrows():
        uncleaned_row = row.to_dict()

        #Take each county name and clean it to be just the county name. Each now are like '.Albany County, New York'
        #This removes the leading period and the ' County, New York' from the string to allow for a nice key
        county_key = uncleaned_row['New York']
        county_key = county_key[1:]
        county_key = county_key.split(' County')[0]

        #Use only the most recent annual estimate from the dataset (July 1, 2023), ignoring the other 4 estimates.
        cleaned_dictionary[county_key] = uncleaned_row[19571216]

    return cleaned_dictionary

def write_bio_data(bio_name, bio_dict):
    print("\tWriting processed biodiversity data to 'data_processed/" + bio_name + ".pkl'")
    time.sleep(0.5)
    # Write processed data with pkl for easy opening in other file
    with open("./data_processed/" + bio_name + ".pkl", 'wb') as file:
        pickle.dump(bio_dict, file)

def write_pop_data(pop_name, pop_dict):
    print("\tWriting processed population data to 'data_processed/" + pop_name + ".pkl'")
    time.sleep(0.5)
    #Write processed data with pkl for easy opening in other file
    with open("./data_processed/" + pop_name + ".pkl", 'wb') as file:
        pickle.dump(pop_dict, file)

#Run cleaning and writing. Called from wf_core.py
def run():
    unprocessed_bio_data_path = "./data_original/biodiversity_data_new_york_counties.csv"
    unprocessed_pop_data_path = "./data_original/population_data_new_york_counties.xlsx"
    cleaned_bio_name = "cleaned_biodiversity_data"
    cleaned_pop_name = "cleaned_population_data"

    # given the location of both datasets, read in the data, transform the data, and write to 'data_processed/'
    process_data(unprocessed_bio_data_path, unprocessed_pop_data_path, cleaned_bio_name, cleaned_pop_name)

if __name__ == '__main__':
    run()