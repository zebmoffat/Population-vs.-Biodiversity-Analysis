__author__ = "Zeb Moffat"
__date__ = "10/22/2024"

import pickle
import numpy as np
import matplotlib.pyplot as plt
import time


def compute_summary_statistics():
    #Gather data for summary statistics, pairwise correlations, and quantitative scatter plots
    counties_population_statistics, documentation_count, years_list, county_dict = quantitative_statistics()

    #Gather qualitative data for plotting histograms
    tax_group_dict, tax_subgroup_dict = qualitative_statistics()

    pairwise_correlations(counties_population_statistics, documentation_count, years_list)

    #Plot scatter plots with quantitative data
    quantitative_plots(county_dict)

    #Plot histograms with qualitative data (Taxonomic groups and subgroups)
    qualitative_plots(tax_group_dict, tax_subgroup_dict)

#Gathers quantitative statistics from data.
def quantitative_statistics():
    #Original population dictionary from data processing file
    original_population_dict = dict()

    original_biodiversity_dict = dict()

    #Dictionary containing population, documentation count, and midpoint year for each county
    county_dict = dict()

    with open('./data_processed/cleaned_population_data.pkl', 'rb') as file:
        original_population_dict = pickle.load(file)

    with open('./data_processed/cleaned_biodiversity_data.pkl', 'rb') as file:
        original_biodiversity_dict = pickle.load(file)

    #Populate county_dict with keys for each county and values for an empty list
    for key in original_population_dict:
        county_dict[key] = list()

    #List for all county populations
    counties_population_statistics = list()

    #Add all populations to list for quantitative feature calculation
    for key in original_population_dict:
        counties_population_statistics.append(original_population_dict[key])
        #Add the population to the county small list
        county_dict[key].append(original_population_dict[key])

    #Sort populations list
    counties_population_statistics.sort()

    #Median of the counties list
    counties_median = ((counties_population_statistics[len(counties_population_statistics)//2 - 1]
                       + counties_population_statistics[len(counties_population_statistics)//2]) // 2)

    #List for the count of biodiversity documentation by each county
    documentation_count = list()

    #For each county, count the number of documentations for each group
    for key in original_biodiversity_dict:
        documentation_count.append(len(original_biodiversity_dict[key]))
        #Add the count for each county small list
        county_dict[key].append(len(original_biodiversity_dict[key]))

    #Sort the counts
    documentation_count.sort()

    #Median of the documentations list
    doc_median = ((documentation_count[len(documentation_count)//2 - 1]
                  + documentation_count[len(documentation_count)//2]) / 2)

    #A dictionary for holding the years of documentation for each county
    bio_years_dict = dict()

    for county in original_biodiversity_dict:
        #Gather the years for each county
        years = list()

        #Go through each list tied to each county
        for array in original_biodiversity_dict[county]:
            years.append(array[5])

        bio_years_dict[county] = years

    for county in bio_years_dict:
        #Filter the list from 0s because those are in place for rows that did not have a recorded year
        bio_years_dict[county] = [x for x in bio_years_dict[county] if x != 0]

        #Take years without the "not available" years and find their midpoint for each county.
        #Then round down
        bio_years_dict[county] = bio_years_dict[county][len(bio_years_dict[county]) // 2]
        #Add midpoint year to the county small list
        county_dict[county].append(bio_years_dict[county])

    #List for all years
    years_list = list()

    #Add each year to list
    for county in bio_years_dict:
        years_list.append(bio_years_dict[county])

    #Sort years
    years_list.sort()

    #Median of the years_list
    years_median = (years_list[len(years_list)//2] + years_list[len(years_list)//2 - 1]) // 2

    #Long string to write to summary.txt and display
    processed_data = ("Summary Statistics\n"
                      "                                       +-------------+-------------+------------+\n"
                      "Quantitative Features                  |   Minimum   |   Maximum   |   Median   |\n"
                      "                                       +-------------+-------------+------------+\n"
                      "Population per County                  |       "
                      + format(counties_population_statistics[0], ',') + " |   "
                      + format(counties_population_statistics[len(counties_population_statistics) - 1], ',')
                      + " |     " + format(counties_median, ',') + " |\n"
                      "Documented Group Count per County      |         " + str(documentation_count[0]) +
                      " |         " + str(documentation_count[len(documentation_count) - 1]) + " |      " +
                    str(doc_median) + " |\n"
                    "Midpoint Documentation Year per County |        " + str(years_list[0]) + " |        "
                    + str(years_list[len(years_list) - 1]) + " |       " + str(years_median) + " |\n"
                      "                                       +-------------+-------------+------------+")
    time.sleep(0.5)
    print("\n----------------------------------------------------------------------------------------------------------"
          "----------------------------------------\n\n" + processed_data)

    #Write to ./data_processed/summary.txt
    with open("./data_processed/summary.txt", "w") as file:
        file.write(processed_data)

    return (counties_population_statistics, documentation_count, years_list, county_dict)

#Use the three summary statistics lists for pairwise correlation saves output to data_processed/correlations.txt
def pairwise_correlations(counties_population_statistics, documentation_count, years_list):
    #Convert lists to numpy arrays
    arr1 = np.array(counties_population_statistics)
    arr2 = np.array(documentation_count)
    arr3 = np.array(years_list)

    #Calculate pairwise correlations between each list
    ppc_vs_ppc = np.corrcoef(arr1, arr1)[0, 1]
    ppc_vs_dgcpc = np.corrcoef(arr1, arr2)[0, 1]
    dgcpc_vs_dgcpc = np.corrcoef(arr2, arr2)[0, 1]
    mdypc_vs_ppc = np.corrcoef(arr3, arr1)[0, 1]
    mdypc_vs_dgcpc = np.corrcoef(arr3, arr2)[0, 1]
    mdypc_vs_mdypc = np.corrcoef(arr3, arr3)[0, 1]

    #Format one string to show all data for file output and console output
    processed_data = ("Pairwise Correlations\n"
                      "                                       +-----------------------+-------------------------------"
                      "----+----------------------------------------+\n                                       | Populat"
                      "ion per County | Documented Group Count per County | Midpoint Documentation Year per County |\n"
                      "                                       +-----------------------+-------------------------------"
                      "----+----------------------------------------+\nPopulation per County                  |" +
                      f"                   {ppc_vs_ppc} |                                   |                         "
                      f"               |"
                      "\nDocumented Group Count per County      |    " + f"{ppc_vs_dgcpc} |                           "
                      f"    " + f"{dgcpc_vs_dgcpc} |                                        |"
                      "\nMidpoint Documentation Year per County |    " + f"{mdypc_vs_ppc} |                " +
                      f"{mdypc_vs_dgcpc} |                                    " + f"{mdypc_vs_mdypc} |"
                      "\n                                       +-----------------------+--------------------------------"
                      "---+----------------------------------------+")
    time.sleep(0.5)
    print("\n----------------------------------------------------------------------------------------------------------"
          "----------------------------------------\n\n" + processed_data + "\n\n--------------------------------------"
          "-----------------------------------------------------------------------------------------------------------"
          "-")

    #Write processed correlations to correlations.txt
    with open("./data_processed/correlations.txt", "w") as file:
        file.write(processed_data)

#Gathers qualitative statistics for taxonomic group and taxonomic subgroup from data.
def qualitative_statistics():
    #Variable for biodiversity dictionary from data processing
    bio_dict = dict()

    #Dictionaris holding taxonomic group and taxonomic subgroup appearance information
    tax_group_dictionary = dict()
    tax_subgroup_dictionary = dict()

    #Load pickle bio data as dictionary
    with open('./data_processed/cleaned_biodiversity_data.pkl', 'rb') as file:
        bio_dict = pickle.load(file)

    #For each county in the biodiversity data
    for key in bio_dict:
        #For each row belonging to that county
        for array in bio_dict[key]:
            #Add the taxonomic group to the dictionary if not already present and set occurrences to 1
            if array[1] not in tax_group_dictionary:
                tax_group_dictionary[array[1]] = 1
            #If present increment occurrences
            else:
                tax_group_dictionary[array[1]] += 1

            #Add the taxonomic group to the dictionary if not already present and set occurrences to 1
            if array[2] not in tax_subgroup_dictionary:
                tax_subgroup_dictionary[array[2]] = 1
            #If present increment occurrences
            else:
                tax_subgroup_dictionary[array[2]] += 1

    #Number of times category is measured, impossible numbers to start that will be changed
    group_most_frequent_number = -1
    group_least_frequent_number = 9999999

    subgroup_most_frequent_number = -1
    subgroup_least_frequent_number = 9999999

    #Find amount most and least categories appear
    for key in tax_group_dictionary:
        if tax_group_dictionary[key] > group_most_frequent_number:
            group_most_frequent_number = tax_group_dictionary[key]
        if tax_group_dictionary[key] < group_least_frequent_number:
            group_least_frequent_number = tax_group_dictionary[key]

    for key in tax_subgroup_dictionary:
        if tax_subgroup_dictionary[key] > subgroup_most_frequent_number:
            subgroup_most_frequent_number = tax_subgroup_dictionary[key]
        if tax_subgroup_dictionary[key] < subgroup_least_frequent_number:
            subgroup_least_frequent_number = tax_subgroup_dictionary[key]

    #Strings holding most and least frequent categories for both groups
    most_frequent_groups = ""
    least_frequent_groups = ""

    most_frequent_subgroups = ""
    least_frequent_subgroups = ""

    #Add all categories to taxonomic group lists that were most or least frequent
    for key in tax_group_dictionary:
        if tax_group_dictionary[key] == group_most_frequent_number:
            if most_frequent_groups == "":
                most_frequent_groups += key
            else:
                most_frequent_groups += ", " + key
        if tax_group_dictionary[key] == group_least_frequent_number:
            if least_frequent_groups == "":
                least_frequent_groups += key
            else:
                least_frequent_groups += ", " + key

    #Add all categories to taxonomic subgroup lists that were most or least frequent
    for key in tax_subgroup_dictionary:
        if tax_subgroup_dictionary[key] == subgroup_most_frequent_number:
            if most_frequent_subgroups == "":
                most_frequent_subgroups += key
            else:
                most_frequent_subgroups += ", " + key
        if tax_subgroup_dictionary[key] == subgroup_least_frequent_number:
            if least_frequent_subgroups == "":
                least_frequent_subgroups += key
            else:
                least_frequent_subgroups += ", " + key

    #Long string to write to summary.txt and display
    processed_data = ("                                       +----------------------+-----------------------------"
                      "------+----------------------------------------------+\n" + "Qualitative Features               "
                      "    | Number of Categories | Most "
                                                           "Frequent"
                      " Category/Categories |      Least Frequent Category/Categories      |\n" + "                   "
                      "                    +"
        "----------------------+-----------------------------------+----------------------------------------------+\n" 
        "Taxonomic Group                        |                   " + str(len(list(tax_group_dictionary.keys()))) +
        " |                             " + most_frequent_groups +
        " |                         " + least_frequent_groups + " |\n" + "Taxonomic Subgroup                     |   "
        "               " + str(len(list(tax_subgroup_dictionary.keys()))) + " |            " + most_frequent_subgroups
        + " |    " + least_frequent_subgroups + " |\n" + "                                       +-------------------"
        "---+-----------------------------------+----------------------------------------------+")

    time.sleep(0.5)
    print(processed_data)

    #Write to ./data_processed/summary.txt
    with open("./data_processed/summary.txt", "a") as file:
        file.write("\n" + processed_data)

    #Return dictionaries for use in histograms
    return (tax_group_dictionary, tax_subgroup_dictionary)

#Create three scatter plots for the quantitative data.
def quantitative_plots(county_dict):

    #Get all keys for plotting
    county_names = list(county_dict.keys())

    #Seperate all values into a list of values
    values = list(county_dict.values())

    #List comprehension to gather each list from values
    populations = [x[0] for x in values]
    documentations = [x[1] for x in values]
    years = [x[2] for x in values]

    #Clear plot
    plt.clf()

    #Plot scatter plot for each county population vs biodiversity documentations
    plt.figure(figsize=(20, 10))
    plt.scatter(populations, documentations)
    plt.xlabel("Population")
    plt.ylabel("Documentations")
    plt.title("County Population vs Biodiversity Documentations")

    #Add labels to scatter
    for i, county_names in enumerate(county_names):
        plt.text(populations[i], documentations[i], county_names, fontsize=9, ha='right', rotation=45)

    plt.subplots_adjust(top=0.98, bottom=0.18)
    plt.tight_layout()

    #plt.show()
    plt.savefig("./visuals/population_vs_biodiversity.png")
    time.sleep(0.5)
    print("\n\tSaved 'population_vs_biodiversity.png' to visuals/")
    #Clear plot
    plt.clf()

    #Plot scatter plot for each county biodiversity documentations vs midpoint documentation year
    plt.figure(figsize=(15, 10))
    plt.scatter(years, documentations)
    plt.xlabel("Midpoint Documentation Year")
    plt.ylabel("Documentations")
    plt.title("County Midpoint Documentation Year vs Biodiversity Documentations")

    #Set x-axis limits from 1990 to 2015
    plt.xlim(1990, 2015)
    # Set x-ticks from 1990 to 2015 and use whole numbers
    plt.xticks(np.arange(1990, 2016, 1))

    plt.subplots_adjust(top=0.97, bottom=0.05, left=0.05, right=0.95)

    #plt.show()
    plt.savefig("./visuals/midpoint_year_vs_biodiversity.png")

    time.sleep(0.5)
    print("\tSaved 'midpoint_year_vs_biodiversity.png' to visuals/")

    #Clear plot
    plt.clf()

    #Plot scatter plot for each county population vs midpoint documentation year
    plt.figure(figsize=(15, 10))
    plt.scatter(populations, years)
    plt.xlabel("Population")
    plt.ylabel("Midpoint Year")
    plt.title("County Population vs Midpoint Documentation Year")

    plt.subplots_adjust(top=0.97, bottom=0.05, left=0.09, right=0.91)

    #plt.show()
    plt.savefig("./visuals/population_vs_midpoint_year.png")

    time.sleep(0.5)
    print("\tSaved 'population_vs_midpoint_year.png' to visuals/")

    #Clear plot
    plt.clf()

#Create two histograms for the qualitative data.
def qualitative_plots(tax_group_dict, tax_subgroup_dict):
    #Clear plot
    plt.clf()

    #Taxonomic group histogram
    plt.figure(figsize=(10, 15))
    plt.bar(list(tax_group_dict.keys()), list(tax_group_dict.values()))
    plt.title("Amount each Taxonomic Group was documented in the State of New York")
    plt.ylabel("Times Taxonomic Group was Documented")
    plt.xlabel("Taxonomic Group")
    plt.xticks(rotation=-90)
    plt.subplots_adjust(top=0.98, bottom=0.18)
    plt.tight_layout()
    #plt.show()
    plt.savefig("./visuals/taxonomic_groups_histogram.png")

    time.sleep(0.5)
    print("\tSaved 'taxonomic_groups_histogram.png' to visuals/")

    #Clear plot
    plt.clf()

    #Taxonomic subgroup histogram
    plt.figure(figsize=(17, 10))
    plt.bar(list(tax_subgroup_dict.keys()), list(tax_subgroup_dict.values()))
    plt.title("Amount each Taxonomic Subgroup was documented in the State of New York")
    plt.ylabel("Times Taxonomic Subgroup was Documented")
    plt.xlabel("Taxonomic Subgroup")
    plt.xticks(rotation=-90)
    plt.tight_layout()
    #plt.show()
    plt.savefig("./visuals/taxonomic_subgroups_histogram.png")

    time.sleep(0.5)
    print("\tSaved 'taxonomic_subgroups_histogram.png' to visuals/")
    #Clear plot
    plt.clf()

#Run computing summary statistics and creating visualizations. Called from wf_core.py
def run():
    compute_summary_statistics()

if __name__ == '__main__':
    run()