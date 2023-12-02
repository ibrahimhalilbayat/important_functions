'''
Script to append a dataframe
by 
Dark Lord İbrahim Halil BAYAT
Fearless, Nameless, Formless and other -less stuff

-----------------------------------------------------
'''

import pandas as pd

# First, we create an empty dataframe 
df = pd.DataFrame(columns=['Column_1', 'Column_2', 'Column_3', 'Column_4']) 


for index in range(16789):
    try:
        data = {'Column_1': index + 1, 
                'Column_2': index + 2,
                'Column_3': index + 3,
                'Column_4': index + 4}
        df_to_append = pd.DataFrame(data, index=[index])
        df = pd.concat([df, df_to_append])
    except:
        pass