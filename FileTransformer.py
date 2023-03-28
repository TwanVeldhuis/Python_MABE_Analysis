import pandas as pd
import sys, os

# Gather all the full paths of the files in the specified folder
root = r'.\mabe_data'
path = os.path.join(root, "targetdirectory")
fullFilePaths = []
for path, subdirs, files in os.walk(root):
    for name in files:
        fullFilePaths.append(os.path.join(path, name))

# loop through all the different files
for file in fullFilePaths:
    # read the files
    LOD_data = pd.read_csv(file)

    # count the number of rows
    row_count = 0
    # iterating over indices
    for row in LOD_data.index:
        row_count += 1

    # if rowcount is less then 500 then duplicate the last row until there are 500 rows
    if row_count < 500:
        row_diff = 500 - row_count
        last_row = LOD_data.tail(1)
        for i in range(row_diff):
            last_row.to_csv(file, mode='a', index=False, header=False)