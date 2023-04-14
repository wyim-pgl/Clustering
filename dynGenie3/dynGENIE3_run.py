#!/usr/bin/env python
from dynGENIE3 import *
import pandas as pd
import numpy as np
import sys

# Check if a filename was passed as an argument
if len(sys.argv) < 3:
    print('Usage: python my_script.py input_file tffile')
    sys.exit(1)

# Get the filename from the command-line argument
filename = sys.argv[1]
tf = sys.argv[2]

# Load the first line of the file into a temporary array to determine the number of columns
with open(filename) as f:
    header = f.readline().rstrip()
    #print(header)
    num_cols = len(header.split('\t')) - 1  # Subtract 1 for the first column
    #print(num_cols)
# Load the contents of the file into a NumPy array, ignoring the first column
# data = np.loadtxt(filename, delimiter='\t', usecols=range(1, num_cols+1))
no_samples = int(num_cols / 3)
#print(no_samples)
x = list(range(1, no_samples + 1))
time_points = [x, x, x]
#print(x)
#print(len(x))
#print(time_points)
#print(len(time_points))

data = pd.read_csv(filename, sep='\t')
gene_names = data.iloc[:, 0].tolist()
total_len=len(gene_names)
#print(total_len)
data = data.to_numpy()
data_tp = np.transpose(data)

ts1 = data_tp[1::3,:]
ts2 = data_tp[2::3,:]
ts3 = data_tp[3::3,:]
TS_data =[ts1,ts2,ts3]
#print(ts1)
#print(len(ts1))
#print(len(ts2))
#print(len(ts3))
#print(len(TS_data))

#ErrorList = list() #List of genes that give error
#ErrorTargetNumber = 0 #Number of those genes

data = pd.read_csv(tf, sep='\t')
regulators = data.iloc[:, 0].tolist()


start= time.time()
#print("gene",x, "is a target", end='\n')
(VIM, alphas, prediction_score, stability_score, treeEstimators) = dynGENIE3(TS_data,time_points, gene_names=gene_names, nthreads=24)
end= time.time()
print ("run dyngenie3 for", (end-start), "sec")

rank = f"{os.path.splitext(filename)[0]}_rank{os.path.splitext(filename)[1]}"
tfrank =  f"{os.path.splitext(filename)[0]}_tfrank{os.path.splitext(filename)[1]}"

start2= time.time()
get_link_list(VIM, gene_names=gene_names,file_name=rank)
get_link_list(VIM, gene_names=gene_names,regulators=regulators, file_name=tfrank)
end2 = time.time()
print ("run getlink for", (end2-start2), "sec")





