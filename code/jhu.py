import os
import argparse
import pickle
import sys
from selection import Selection
from okr_types import ClassificationLabel, FeatureVector, Instance
from bs4 import BeautifulSoup

def load_data(filename, mode):
    instances = [] # Initialize empty instances array
    
    # This where BeautifulSoup saves time
    with open(filename) as reader:
        soup = BeautifulSoup(reader, "xml")
    # Find and display all organizations to user
    organizations = soup.find_all("Organization")
    #print(organizations)
    for org in organizations:
        org_name = org.find("name")
        label_string = org_name.string
        if mode == 0:
            print(label_string)
            print("\n")
        
        label = ClassificationLabel(label_string)
        feature_vector = FeatureVector()
        
        # Find organization of interest
        org_tag = soup.find("name", string=label_string)
        
        # Find building (i.e. site) associated with organization of interest
        hasSite = org_tag.next_sibling.next_sibling
        
        tags = ["name", "geo"]
        for index in range(len(tags)):
            value = hasSite.find(tags[index])
            feature_vector.add(index, value)
        
        instance = Instance(feature_vector, label)
        instances.append(instance)
        
    return instances # Return array of all JHU organizations with their corresponding features


def get_args():
    # our user interface will have 2 modes: select and generate
    # select: where the user chooses the desired major(s)
    # generate: where our code generates coordinates of the buildings related to the major(s)
    parser = argparse.ArgumentParser(description="This is the main test harness for our algorithms.")

    parser.add_argument("--data", type=str, required=True, help="The data to use for selecting or generating.")
    parser.add_argument("--mode", type=str, required=True, choices=["select", "generate"], 
                        help="Operating mode: select or generate.")
    parser.add_argument("--org-file", type=str, required=True,
                        help="The name of the organization (i.e. model) file to create/load.")
    parser.add_argument("--results-file", type=str, help="The results file to create.")

    # This is where new command line options are added
    parser.add_argument("--org_of_interest", type=str, help="The organization in which you are interested.", default="admissions")
    parser.add_argument("--number_of_majors", type=int, help="The number of majors you are considering.", default=1)
    parser.add_argument("--feature_of_interest", type=str, help="The feature in which you are interested.", default="building")
    
    args = parser.parse_args() # Create variable args, and set args = arguments obtained from parsing a command line argument using an Argument Parser
    check_args(args) # Check which arguments user gives to determine course of action

    return args # Return arguments obtained from parsing a command line argument


def check_args(args):
    if args.mode.lower() == "generate": # if in generate mode
        if args.results_file is None: # if no results file
            raise Exception("--results-file should be specified in mode \"generate\"") # ask user to specify results file
        if not os.path.exists(args.model_file): # if org file does not exist
            raise Exception("organization file specified by --org-file does not exist.") # tell user model file does not exist


def select(instances, org_of_interest, number_of_majors):
    # Select the organization model to run on "data"
    # This is where new algorithms are added that subclass Generator
    organization = Selection() # Create variable organization, and set organization = the (instance of?) Selection() class
        
    organization.select(instances, org_of_interest, number_of_majors) # Run the Selection() class's select function
    
    return organization # Return (instance of?) Selection() class


def write_results(generator, instances, feature_of_interest, results_file):
    try:
        with open(results_file, 'w') as writer:
            for instance in instances:
                label = generator.generate(instance, feature_of_interest)
                    
                writer.write(str(label))
                writer.write('\n')
    except IOError:
        raise Exception("Exception while opening/writing file for writing generated labels: " + results_file)


def main():
    args = get_args() # create variable args, and set args = arguments obtained from parsing a command line argument (output of get_args() fcn)
    
    if args.mode.lower() == "select":
        # Load the data in select mode.
        instances = load_data(args.data, 0) # args.data = jhu.xml; thus, init variable instances = array of JHU orgs (output of load_data function)
        
        # Select the organization (i.e. model).
        generator = select(instances, args.org_of_interest, args.number_of_majors) # Create variable generator, and set generator = ___ (output of select function)
        try:
            with open(args.org_file, 'wb') as writer:
                pickle.dump(generator, writer)
        except IOError:
            raise Exception("Exception while writing to the organization file.")        
        except pickle.PickleError:
            raise Exception("Exception while dumping pickle.")
            
    elif args.mode.lower() == "generate":
        # Load the data in generate mode.
        instances = load_data(args.data, 1) # args.data = jhu.xml; thus, init variable instances = array of JHU orgs (output of load_data function)
        
        generator = None
        # Load the model.
        try:
            with open(args.org_file, 'rb') as reader:
                generator = pickle.load(reader)
        except IOError:
            raise Exception("Exception while reading the organization file.")
        except pickle.PickleError:
            raise Exception("Exception while loading pickle.")
            
        write_results(generator, instances, args.feature_of_interest, args.results_file)
    else:
        raise Exception("Unrecognized mode.")

if __name__ == "__main__":
    main()

