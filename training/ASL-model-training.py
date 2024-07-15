import os
import tensorflow as tf
import pathlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset = tf.data.TFRecordDataset(filenames = [r'C:/Users/laksh/Documents/ASL/ASL-Identifier/asldb/test/Letters.tfrecord']) # type: ignore
for record in dataset.take(10):
  print(repr(record))

  