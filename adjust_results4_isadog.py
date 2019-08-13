# PROGRAMMER:Gustavo Cedeno
# DATE CREATED:01.01.2019
# REVISED DATE:
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results
#          dictionary to indicate whether or not the pet image label is of-a-dog,
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the
#          dog name (from dognames.txt) and the 'value' is one. If a label is
#          found to exist within this dictionary of dog names then the label
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog.
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main.
#           This function uses the extend function to add items to the list
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the
#           label isn't a dog.
#
#
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly
    classified images 'as a dog' or 'not a dog' especially when not a match.
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
                    List. Where the list will contain the following items:
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has
               one dog name per line dog names are all in lowercase with
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names
               associated with that breed (ex. maltese dog, maltese terrier,
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    #New dictionary containing the list of dogs in dognames.txt
    #data structure for dog names is a dictionary with the key as the dog name
    # and a value of 1 (arbitrary value)
    #If a dog name already exists in dognames_dic print a Warning statement
    # because you shouldn't find any duplicate dog names in dognames.txt
    dognames_dic={}
    with open(dogfile) as dogs:
        for line in dogs:
            rline=line.rstrip('\n')
            if rline not in dognames_dic:
                dognames_dic[rline]=1
            else:
                print("** Warning: Key=", rline,
               "already exists in dognames_dic with value =",
               dognames_dic[rline])
    #Debugging print statements
    #print('\nDog Names\n',dognames_dic)

    #Checking if the Pet Image Label and the Classifier Label from the results_dic
    #are in the dognames_dic as keys
    #adjust the results dictionary (results_dic) to account for when labels were
    #correctly or incorrectly classified as dogs.
    for label, value in results_dic.items():
#index 3 = 0/1 where 1= Pet Image Label is a dog, 0 = Pet Image Label isn't a dog (ex: 1)
        if value[0] in dognames_dic.keys():
            results_dic[label].append(1)
        else:
            results_dic[label].append(0)
#index 4 = 0/1 where 1= Classifier Label is a dog, 0 = Classifier Label isn't a dog (ex: 1)
        if value[1] in dognames_dic.keys():
            results_dic[label].append(1)
        else:
            results_dic[label].append(0)
#Debugging print statements
    #print('\n New results_dic:\n',results_dic)
