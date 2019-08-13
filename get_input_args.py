# PROGRAMMER:Gustavo Cedeno
# DATE CREATED: 29.12.2018
# REVISED DATE:
# PURPOSE: Create a function that retrieves the following 3 command line inputs
#          from the user using the Argparse Python module. If the user fails to
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

#
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's
    argparse module to created and defined these 3 command line arguments. If
    the user fails to provide some or all of the 3 arguments, then the default
    values are used for the missing arguments.
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object
    """
    # Creates Argument Parser object named parser
    parser = argparse.ArgumentParser()

    # Argument 1: that's a path to a folder
    parser.add_argument('--dir', type = str, default = 'pet_images/',
                    help = 'path to the folder of pet images')
    # Argument 2: The CNN model architecture to use (resnet, alexnet or vgg)
    parser.add_argument('--arch', type = str, default = 'vgg',
                    help = 'CNN model architecture to use')
    # Argument 3: File that contains the list of valid dognames
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt',
                    help = 'list of valid dognames')

    #Assign the in_args variable to parse_args and return their values
    in_arg = parser.parse_args()

    # Replace None with parser.parse_args() parsed argument collection that
    # you created with this function

    return in_arg
