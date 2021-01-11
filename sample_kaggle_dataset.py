import numpy as np
import shutil
import os

basepath = "/home/rafa/Downloads/chest_xray"
basepath = os.path.join(basepath, "train", "PNEUMONIA")
filenames = [file for file in os.listdir(basepath)]

outputpath = "data/pneumonia"

filenames = np.random.choice(filenames, size=200, replace=False)

for (i, filename) in enumerate(filenames):
    filename = filename.split(os.path.sep)[-1]
    imagepath = os.path.join(basepath, filename)
    imageoutputpath = os.path.join(outputpath, filename)

    # copy the image to new directory
    shutil.copy2(imagepath, imageoutputpath)