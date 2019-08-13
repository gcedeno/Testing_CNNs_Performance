# Description
This repository contains code and associated files corresponding to Udacity's introductory project for the AI Programming with Python Nanodegree program. This repository consists of the solution for the Image Classification Project. The goal of the project is to develop several python functions to determine which image classification algorithm works the best on classifying images as "dogs" and "not dogs".

For this image classification task an image classification application using a deep learning model called a convolutional neural network (often abbreviated as CNN) is used. CNNs work particularly well for detecting features in images like colors, textures, and edges; then using these features to identify objects in the images. A CNN that has already learned the features from a giant dataset of 1.2 million images called ImageNet is given (No training is required, functions implemented only for predictions). There are different types of CNNs that have different structures (architectures) that work better or worse depending on the used criteria. With this project, three different architectures (AlexNet, VGG, and ResNet) were explored and determined which one worked the best for the application.

A classifier function in `classifier.py` that allows using these CNNs to classify the images is provided. The `test_classifier.py` file contains an example program that demonstrates how to use the classifier function. For this project, the focus is on developing Python code to complete these tasks using the classifier function.


### Programming Project -Original Project Files (No Solutions)
* [Intro to Python Project - Classifying Pet Images:](https://github.com/udacity/AIPND-revision/tree/master/intropyproject-classify-pet-images "Classifying Pet Images Project") Determine which CNN architecture model works best at classifying images of dogs and their breeds.


## Dependencies

Each directory has a `requirements.txt` describing the minimal dependencies required to run the notebooks in that directory.

### pip

To install these dependencies with pip, you can issue `pip3 install -r requirements.txt`.
