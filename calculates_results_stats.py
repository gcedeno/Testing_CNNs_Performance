#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#
# PROGRAMMER:Gustavo Cedeno
# DATE CREATED:01.02.2019
# REVISED DATE:
# PURPOSE: Create a function calculates_results_stats that calculates the
#          statistics of the results of the programrun using the classifier's model
#          architecture to classify the images. This function will use the
#          results in the results dictionary to calculate these statistics.
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best'
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the
#          how to calculate the counts and percentages for this function.
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics
#          (either a percentage or a count) where the key is the statistic's
#           name (starting with 'pct' for percentage or 'n' for count) and value
#          is the statistic's value.  This dictionary should contain the
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create
#       with this function
#
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images. Then puts the results statistics in a
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the classroom Item XX Calculating Results for details
                     on how to calculate the counts and statistics.
    """
    # Replace None with the results_stats_dic dictionary that you created with
    # this function
    #creating the results statistics dictionary
    results_stats_dic={}
    #Z: Number of images
    n_images = len(results_dic)
    #definig and setting counters to 0
    n_correct_dogs=0
    n_dog_img=0
    n_correct_nondog_match=0
    n_nondog_images=0
    n_correct_breed=0
    n_label_match=0
    #Calculating the counts from the results dictionary
    for key in results_dic:
        #A: Number of Correct Dog matches / Both labels are dogs
        if results_dic[key][3]==1 and results_dic[key][4]==1:
            n_correct_dogs+=1
        #B: Number of dog images/Pet Label is a dog
        if results_dic[key][3]==1:
            n_dog_img+=1
        #C: Number of Correct Non-Dog matches/Both Labels are not dogs
        if results_dic[key][3]==0 and results_dic[key][4]==0:
            n_correct_nondog_match+=1
        #D: Number of Non Dog Images/Pet Label is NOT a dog
        if results_dic[key][3]==0:
            n_nondog_images+=1
        #E: Number of Correct Breed matches/Pet Label is dog and Labels match
        if results_dic[key][3]==1 and results_dic[key][2]==1:
            n_correct_breed+=1
        #Y: Number of label matches
        if results_dic[key][2]==1:
            n_label_match+=1

    results_stats_dic.update({'n_images':n_images,'n_correct_dogs':n_correct_dogs,
                  'n_dogs_img':n_dog_img,'n_correct_notdogs':n_correct_nondog_match, #change key name
                 'n_notdogs_img':n_nondog_images,'n_correct_breed':n_correct_breed,
                 'n_label_match':n_label_match})
    #Debugging print statements
    #print('\n Results Statistics Dictionary\n',results_stats_dic)

    #Objective_1_a: Percentage of Correctly Classified Dog Images = A/B*100
    #A. Correctly classified dog images
    #B. Number of dog images
    if n_dog_img !=0:
        pct_correct_dogs= (n_correct_dogs/n_dog_img)*100

    else:
        pct_correct_dogs=0
    #Objective_1_b: Percentage of Correctly Classified Non-Dog Images = C/D*100
    #C Correctly classified NOT a dog images.
    #D Number of NOT a dog images
    if n_nondog_images !=0:
        pct_correct_nondogs= (n_correct_nondog_match/n_nondog_images)*100

    else:
        pct_correct_nondogs=0
    #Objective_2_: Percentage of Correctly Classified Dog Breeds = E/B * 100
    #E Correctly classified as a particular breed of dog images.
    #B. Number of dog images
    if n_dog_img !=0:
        pct_correct_breed= (n_correct_breed/n_dog_img)*100

    else:
        pct_correct_breed=0
    #Optional Y: Percentage Label Matches ( regardless if they're a dog): Y/Z * 100
    #Y Number of label matches
    #Z Number of images
    if n_images !=0:
        pct_label_match= (n_label_match/n_images)*100

    else:
        pct_label_match=0
    # Updating the stats_results dictionary with the new calculated percentages
    results_stats_dic.update({'pct_correct_dogs':pct_correct_dogs,'pct_correct_notdogs':pct_correct_nondogs,
            'pct_correct_breed':pct_correct_breed, 'pct_label_match':pct_label_match})
    #Debugging print statements
    #print('\n Results Statistics Dictionary\n',results_stats_dic)

    return results_stats_dic
