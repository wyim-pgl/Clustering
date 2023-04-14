# Clustering

## Sort column by name
```
python sort_column_name.py CL_TPM.tsv
python sort_column_name.py DL_TPM.tsv
```
## CAM and C3 seperate
```
python matrix_sperate.py CL_TPM.tsv
python matrix_sperate.py DL_TPM.tsv
```
## filter file <24 TPM
```
dynGENIE3_filter.py CL_TPM_sorted_filtered_C3.tsv CL_TPM_sorted_filtered_C3
dynGENIE3_filter.py CL_TPM_sorted_filtered_CAM.tsv CL_TPM_sorted_filtered_CAM
dynGENIE3_filter.py DL_TPM_sorted_filtered_C3.tsv DL_TPM_sorted_filtered_C3
dynGENIE3_filter.py DL_TPM_sorted_filtered_CAM.tsv DL_TPM_sorted_filtered_CAM
```
## submit
```
 sbatch -c 32 --mem=64g --wrap="dynGENIE3_run.py DL_TPM_sorted_filtered_C3 tf_list.txt"
 sbatch -c 32 --mem=64g --wrap="dynGENIE3_run.py DL_TPM_sorted_filtered_CAM tf_list.txt"
 sbatch -c 32 --mem=64g --wrap="dynGENIE3_run.py CL_TPM_sorted_filtered_CAM tf_list.txt"
 sbatch -c 32 --mem=64g --wrap="dynGENIE3_run.py CL_TPM_sorted_filtered_C3 tf_list.txt"
```
 
