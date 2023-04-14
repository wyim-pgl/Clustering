import pandas as pd
import os
import sys

filename = sys.argv[1]

# read input file
df = pd.read_csv(filename, sep='\t')

# extract columns containing 'C3'
c3_cols = [col for col in df.columns if 'C3' in col]

# extract columns containing 'CAM'
cam_cols = [col for col in df.columns if 'CAM' in col]

# create new dataframes with first column and the C3/CAM columns
if len(c3_cols) > 0:
    c3_df = df[[df.columns[0]] + c3_cols]
    c3_filename = os.path.splitext(filename)[0] + '_C3.tsv'
    c3_df.to_csv(c3_filename, sep='\t', index=False)
    print(f"Saved C3 data to {c3_filename}")
else:
    print("No C3 columns found in input file")

if len(cam_cols) > 0:
    cam_df = df[[df.columns[0]] + cam_cols]
    cam_filename = os.path.splitext(filename)[0] + '_CAM.tsv'
    cam_df.to_csv(cam_filename, sep='\t', index=False)
    print(f"Saved CAM data to {cam_filename}")
else:
    print("No CAM columns found in input file")

