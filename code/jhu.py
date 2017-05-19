import os
import argparse
import pickle
import sys
from selection import Selection
from okr_types import ClassificationLabel, FeatureVector, Instance
from bs4 import BeautifulSoup

def load_data(filename):
    # This where BeautifulSoup saves time
    with open(filename) as reader:
        soup = BeautifulSoup(reader, "xml")
    # Find and display all organizations to user
    organizations = soup.find_all("Organization")
    return organizations

def print_org_names(organizations):
    #print(organizations)
    for org in organizations:
        print(org.find("foaf:name").string.capitalize())
        
    return

def get_args():
    # our user interface will have 2 modes: select and generate
    # select: where the user chooses the desired major(s)
    # generate: where our code generates coordinates of the buildings related to the major(s)
    parser = argparse.ArgumentParser(description="This is the main test harness for our algorithms.")
    parser.add_argument("--data", type=str, required=True, help="The data to use for selecting or generating.")
    args = parser.parse_args() # Create variable args, and set args = arguments obtained from parsing a command line argument using an Argument Parser
    return args # Return arguments obtained from parsing a command line argument

def main():
    args = get_args() # create variable args, and set args = arguments obtained from parsing a command line argument (output of get_args() fcn)

    organizations = load_data(args.data)

    print_org_names(organizations)

    majors = raw_input('Enter your major names, separated by commas: ')
    majors = majors.split(",")
    for i in range(len(majors)):majors[i] = majors[i].lower().strip()
    
    selected_orgs = []
    for org in organizations:
        if org.find("name").string.lower() in majors:
            selected_orgs.append(org)

    all_features = ["building", "location"]
    for feature in all_features:
        print(feature.capitalize())
    features = raw_input("Enter the information you want to retrieve about these" \
                     + " majors, separated by commas: ")
    features = features.split(",")
    for i in range(len(features)):features[i] = features[i].lower().strip()
    
    
    for org in selected_orgs:
        print(org.find("name").string.capitalize() + ":")

        for feature in features:
            str = "\t" + feature.capitalize() + "=" 
            if (feature == "building"):
                str += org.find("hasSite").find("name").string.capitalize()
            elif (feature == "location"):
                str += org.find("hasSite").find("geo").string.capitalize()
            print(str)
    
if __name__ == "__main__":
    main()

