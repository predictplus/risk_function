import pandas as pd
import os
import glob
import csv

file_extension = '.csv'
path = input("Enter the path to the folder containing the CSV files: ")
os.chdir(path)
folders = len(next(os.walk(path))[1])
dirs = ([name for name in os.listdir(".") if os.path.isdir(name)])
for j in dirs:
    os.chdir(path+j)
    all_filenames = [i for i in glob.glob(f"*{file_extension}")]
    print(all_filenames)
    combined_data = pd.concat([pd.read_csv(f, delimiter = ',', low_memory=False, encoding = "cp1252") for f in all_filenames])
    print(len(combined_data))
    os.chdir(path)
    combined_data.to_csv(all_filenames[0][0:-9]+'.csv', index = False,)
    del(all_filenames,combined_data)
