import pandas as pd
import urllib.request
import zipfile
import os

url = "https://github.com/robintux/Datasets4StackOverFlowQuestions/raw/master/Cancer_Pulmon.zip"
urllib.request.urlretrieve(url, "Cancer_Pulmon.zip")

with zipfile.ZipFile("Cancer_Pulmon.zip", "r") as zip_ref:
    zip_ref.extractall(".")

df = pd.read_csv("Cancer_Pulmon.csv")

print(df.info())
