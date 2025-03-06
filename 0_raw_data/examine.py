import pandas as pd

# Load the data
data = pd.read_csv('dataset_ms2_c.csv')


# Find rows where 'CP' is 0 but 'CM_morph' and 'CP_morph' is not 0
filtered_data = data[(data['CP'] == '0') & (data['CM_morph'] != '0') & (data['CP_morph'] != '0')]

# Check if there are any such rows and print the index if they exist
if not filtered_data.empty:
    print(filtered_data.index.tolist())
else:
    print('done')



