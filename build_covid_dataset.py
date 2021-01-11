import pandas as pd
import shutil
import os


basepath = "/home/rafa/Downloads/covid-chestxray-dataset"
metadatapath = os.path.join(basepath, "metadata.csv")

outputpath = "data/covid"

df = pd.read_csv(metadatapath)

for (i, row) in df.iterrows():
    # get COVID19 and PA x-rays
    if row["finding"] != "Pneumonia/Viral/COVID-19" or row["view"] != "PA":
        continue

    # build the path to the input image file
    imagepath = os.path.join(basepath, "images", row["filename"])

    if not os.path.exists(imagepath):
        continue

    filename = row["filename"].split(os.path.sep)[-1]
    imageoutputpath = os.path.join(outputpath, filename)

    # copy the image to new directory
    shutil.copy2(imagepath, imageoutputpath)