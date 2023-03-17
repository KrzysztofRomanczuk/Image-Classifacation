import cv2 as cv
import numpy as np
import matplotlib as plt
from tensorflow import keras, layers

(training_images, training_labels), (testing_images, testing_labels) = keras.datasets.cifar10.load_data()
training_images, testing_images / training_images / 255, testing_images / 255

