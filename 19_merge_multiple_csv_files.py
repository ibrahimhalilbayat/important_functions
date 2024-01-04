'''
Script to merge csv files into a dataframe
by 
Dark Lord İbrahim Halil BAYAT
Fearless, Nameless, Formless and other -less stuff

-----------------------------------------------------
'''


import os 
import pandas as pd


PATH = ''

def process_line(line):
    values = list(map(float, line.split(',')))
    return {
        'Time': values[0],
        'ID': values[1],
        'Data': values[2:]
    }


df = pd.DataFrame(columns = ['Time', 'ID', 'Data'])
for csv_file in sorted(os.listdir(PATH)):
    with open(PATH+csv_file, 'r') as file:
        lines = file.readlines()

    df_for_now = pd.DataFrame([process_line(line) for line in lines])

    df = pd.concat([df, df_for_now], axis=0, ignore_index=True)

df.to_csv(PATH+'concated_data.csv', index=False)

print(f"Data is saved as concated_data.csv. The path is: {PATH}. \n Shape of data is: {df.shape}")
