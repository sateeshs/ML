from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datetime import datetime
import os
import random
import threading

import numpy as np
import tensorflow as tf

img_rows=64
img_cols=64

def create_dataset():
    filenames = tf.constant();
    labels = tf.constant([0,1])
    dataset = tf.data.Dataset.from_tensor_slices((filenames,labels))
    dataset = dataset.shuffle(len(filenames))
    dataset = dataset.map(parse_function,num_parallel_calls=4)
    dataset = dataset.map(train_preprocess, num_parallel_calls=4)
    dataset = dataset.batch(batch_size)
    dataset = dataset.prefetch(1)
    return dataset

def parse_function(filename, label):
    """
    1. read the content of the file
    2. decode using jpeg format
    3. convert to float values in [0, 1]
    4. resize to size (64, 64)
    """
    image_string = tf.read_file(filename)
    # Don't use tf.image.decode_image, or the output shape will be undefined
    image = tf.image.decode_jpeg(image_string, channels=3)

    # This will convert to float values in [0, 1]
    image = tf.image.convert_image_dtype(image, tf.float32)

    resized_image = tf.image.resize_images(image, [img_rows, img_cols])
    return resized_image, label

def train_preprocess(image,label):
    """
    1. Horizontally flip the image with probability 1/2
    2. Apply random brightness and saturation
    """
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_brightness(image, max_delta=32.0 / 225.0)
    image = tf.image.random_saturation(image, lower=0.5, upper=1.5)

    # Make sure the image is still in [0, 1]
    image = tf.clip_by_value(image, 0.0, 1.0)

    return image, label
