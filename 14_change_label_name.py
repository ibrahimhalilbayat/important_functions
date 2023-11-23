'''
Script to change the label names 
by 
Dark Lord İbrahim Halil BAYAT
Fearless, Nameless, Formless and other -less stuff

-----------------------------------------------------
Steps:
    1- Enter the path of directory that contains json files
    2- Enter the old label and new label
    3- Run the script
    4- Go and live a happy day 
'''


import os 
import json 

THE_PATH = ''
OLD_LABEL = 'anatar'
NEW_LABEL = 'sauron'

for json_file in os.listdir(THE_PATH):
    if json_file.endswith('.json'):
        with open(THE_PATH + "/" + json_file) as f:
            try:
                data = json.load(f)
            
            except Exception as e:
                print(f"An exception occured: {e}")

        
        for shape in data['shapes']:
            if shape['label'] == OLD_LABEL:
                shape['label'] = NEW_LABEL
            else:
                print(f"Couldnt change {OLD_LABEL} to {NEW_LABEL}")
            
        json_file = THE_PATH + "/" + json_file
        save_file = open(json_file, "w")
        json.dump(data, save_file) 
        save_file.close()
