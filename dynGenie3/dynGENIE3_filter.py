#!/usr/bin/env python
import sys
import numpy
import pandas as pd

# Read file from command line argument
file = sys.argv[1]
df = pd.read_csv(file, delimiter='\t')

# Remove rows with sum less than 24
rows_to_drop = []
for index, row in df.iterrows():
    if row[1:].sum() < 24:
        rows_to_drop.append(index)

df.drop(rows_to_drop, axis=0, inplace=True)

# Save the filtered data to a new file
new_file = sys.argv[2]
df.to_csv(new_file, sep='\t', index=False)
