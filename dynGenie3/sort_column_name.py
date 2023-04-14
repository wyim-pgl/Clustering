#!/usr/bin/env python
import pandas as pd
import sys
import os
import natsort

# get the input filename from the command line argument
filename = sys.argv[1]

# read the data into a pandas DataFrame
df = pd.read_csv(filename, sep='\t')

# get a list of column names excluding the first column
cols = list(df.columns[1:])

# sort the columns based on column name using natsort
cols_sorted = natsort.natsorted(cols)

# create a new DataFrame with the sorted columns
df_sorted = df[['gene_id'] + cols_sorted]

# save the sorted DataFrame to a new file
new_filename = f"{os.path.splitext(filename)[0]}_sorted{os.path.splitext(filename)[1]}"
df_sorted.to_csv(new_filename, sep='\t', index=False)

# print a confirmation message
print(f"The file '{filename}' has been sorted using neutral number sort and saved to '{new_filename}'.")

