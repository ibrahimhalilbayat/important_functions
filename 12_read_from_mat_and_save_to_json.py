import h5py
import json
import numpy as np
from time import time

def recursive_read(h5_obj, output_dict):
    for key in h5_obj.keys():
        if isinstance(h5_obj[key], h5py.Dataset):
            # Check if the data is a reference object, if so skip it
            if h5py.check_dtype(ref=h5_obj[key].dtype):
                continue
            # If it's a dataset, convert its value to a nested list before adding it to the data dictionary
            output_dict[key] = h5_obj[key][()].tolist()
        elif isinstance(h5_obj[key], h5py.Group):
            # If it's a group, recursively read the group
            output_dict[key] = {}
            recursive_read(h5_obj[key], output_dict[key])


begin = time()

# Open the mat file
with h5py.File('dl-gG-newdata/v2/Data_v2.mat', 'r') as f:
    print("The file is read")
    # Loop over all keys in the file
    data_dict = {}
    print("Ready to operate the function")
    recursive_read(f, data_dict)

# Print the data dictionary
print("------------------------------ THE DATA  -------------------------------------")
#print(data_dict)

with open('v2_input_data_dict.json', 'w') as handle:
    json.dump(data_dict, handle)

end = time()
print("DURATION: {:.2f} seconds".format(end - begin))
