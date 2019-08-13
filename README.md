# Description
This repository consists of the solution for the Image Classification Project of Udacity's AI Programming with Python ND. The goal of the project is to develop several python functions to determine which image classification algorithm works the best on classifying images as "dogs" and "not dogs".

For this image classification task an image classification application using a deep learning model called a convolutional neural network (often abbreviated as CNN) is used. CNNs work particularly well for detecting features in images like colors, textures, and edges; then using these features to identify objects in the images. A CNN that has already learned the features from a giant dataset of 1.2 million images called ImageNet is given (No training is required, functions implemented only for predictions). There are different types of CNNs that have different structures (architectures) that work better or worse depending on the used criteria. With this project, three different architectures (AlexNet, VGG, and ResNet) were explored and determined which one worked the best for the application.

A classifier function in `classifier.py` that allows using these CNNs to classify the images is provided. The `test_classifier.py` file contains an example program that demonstrates how to use the classifier function. For this project, the focus is on developing Python code to complete these tasks using the classifier function.


### Program Description and Usage
The program classifies pet images using a pretrained CNN model, compares these classifications to the true identity of the pets in the images(labels), and summarizes how well the CNN performed on the image classification task. With this program we will be comparing the performance of 3 different CNN model architectures to determine which provides the 'best' classification.

Use argparse Expected Call with <> indicating expected user input:
      python check_images.py --dir <directory with images> --arch <model>
             --dogfile <file that contains dognames>

   Example call:
    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt


## Dependencies

The main libraries with corresponding versions to run the code can be found in `requirements.txt` describing the minimal dependencies required to run the code in the directory.

### pip

To install these dependencies with pip, you can run `pip3 install -r requirements.txt` from the command line.
