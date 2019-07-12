#Train a model
from datetime import datetime
import os
import random
import sys
import threading


import numpy as np
import tensorflow as tf

class TrainModel:

    def __init__(self):
        # Create a single Session to run all image coding calls.
        self._sess = tf.Session()
