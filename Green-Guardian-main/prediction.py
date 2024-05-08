import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk("D://Desktop//Waste_Management//DATASET"):
    for filename in filenames:
        os.path.join(dirname, filename)


train_organic_dir = os.path.join("D://Desktop//Waste_Management//DATASET//TRAIN//O")

# Directory with training recycle images
train_recycle_dir = os.path.join("D://Desktop//Waste_Management//DATASET//TRAIN//R")

# Directory with test organic images
test_organic_dir = os.path.join("D://Desktop//Waste_Management//DATASET//TEST//O")

# Directory with test recycle images
test_recycle_dir = os.path.join("D://Desktop//Waste_Management//DATASET//TEST/R")

# Directory with validation organic images
val_organic_dir = 'D://Desktop//Waste_Management//DATASET//VALIDATION//O'

# Directory with validation recycle images
val_recycle_dir = 'D://Desktop//Waste_Management//DATASET//VALIDATION//R'

if not os.path.exists(val_organic_dir):
    os.makedirs(val_organic_dir)
    
#if not os.path.exists(val_recycle_dir):
    os.makedirs(val_recycle_dir)

import os
from sklearn.model_selection import train_test_split
from shutil import copyfile

val_size = 0.2 

if not os.listdir(val_organic_dir) and not os.listdir(val_recycle_dir):
    train_organic, val_organic = train_test_split(os.listdir(train_organic_dir), test_size=val_size, random_state=21946201)
    train_recycle, val_recycle = train_test_split(os.listdir(train_recycle_dir), test_size=val_size, random_state=21946201)

    for organic in val_organic:
        src_path = os.path.join(train_organic_dir, organic)
        dst_path = os.path.join(val_organic_dir, organic)
        copyfile(src_path, dst_path)

    for recycle in val_recycle:
        src_path = os.path.join(train_recycle_dir, recycle)
        dst_path = os.path.join(val_recycle_dir, recycle)
        copyfile(src_path, dst_path)
else:
    print("Data validation is exist.")


train_organic_names = os.listdir(train_organic_dir)
print(f'TRAIN SET ORGANIC: {train_organic_names[:10]}')

train_recycle_names = os.listdir(train_recycle_dir)
print(f'TRAIN SET RECYCLE: {train_recycle_names[:10]}')

test_organic_names = os.listdir(test_organic_dir)
print(f'TEST SET ORGANIC: {test_organic_names[:10]}')

test_recycle_names = os.listdir(test_recycle_dir)
print(f'TEST SET RECYCLE: {test_recycle_names[:10]}')

val_organic_names = os.listdir(val_organic_dir)
print(f'VAL SET ORGANIC: {val_organic_names[:10]}')

val_recycle_names = os.listdir(val_recycle_dir)
print(f'VAL SET RECYCLE: {val_recycle_names[:10]}')


print(f'total training organic images: {len(os.listdir(train_organic_dir))}')
print(f'total training recycle images: {len(os.listdir(train_recycle_dir))}')
print(f'total test organic images: {len(os.listdir(test_organic_dir))}')
print(f'total test recycle images: {len(os.listdir(test_recycle_dir))}')
print(f'total validation organic images: {len(os.listdir(val_organic_dir))}')
print(f'total validation recycle images: {len(os.listdir(val_recycle_dir))}')


#%matplotlib inline

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Parameters for our graph; we'll output images in a 4x4 configuration
nrows = 4
ncols = 4

# Index for iterating over images
pic_index = 0

# Set up matplotlib fig, and size it to fit 4x4 pics
fig = plt.gcf()
fig.set_size_inches(ncols * 4, nrows * 4)

pic_index += 8
next_horse_pix = [os.path.join(train_organic_dir, fname)
                for fname in train_organic_names[pic_index-8:pic_index]]
next_human_pix = [os.path.join(train_recycle_dir, fname)
                for fname in train_recycle_names[pic_index-8:pic_index]]

for i, img_path in enumerate(next_horse_pix+next_human_pix):
  # Set up subplot; subplot indices start at 1
  sp = plt.subplot(nrows, ncols, i + 1)
  sp.axis('Off') # Don't show axes (or gridlines)

  img = mpimg.imread(img_path)
  plt.imshow(img)

plt.show()

import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.summary()