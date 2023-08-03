import json
import numpy as np

##### SAVING NUMPY AS JSON ##########################################################################

# Assuming you have your numpy array. Let's call it np_array
np_array = np.random.rand(100, 6, 4, 18)  # Just a placeholder, replace with your array

# Convert the numpy array to a nested list
nested_list = np_array.tolist()

# Now we can save the list to a JSON file
with open('first.json', 'w') as json_file:
    json.dump(nested_list, json_file)

##### READING JSON BACK AS NUMPY ####################################################################

# Open the JSON file and load the data
with open('first.json', 'r') as json_file:
    data = json.load(json_file)

# Convert the data to a numpy array
np_array = np.array(data)

# Now np_array contains the data from the JSON file