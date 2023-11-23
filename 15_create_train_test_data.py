'''
Script to change the label names 
by 
Dark Lord İbrahim Halil BAYAT
Fearless, Nameless, Formless and other -less stuff

-----------------------------------------------------
Steps:
    1- Enter the path of directory that contains all image and txt files
    2- Adjust the interval
    3- Run the script
    4- Go and live a happy day 
'''

import os 

THE_PATH = ""
INTERVAL = 10

if 'dataset' not in os.listdir():
    os.mkdir('dataset')
    os.mkdir('dataset/images')
    os.mkdir('dataset/images/train')
    os.mkdir('dataset/images/val')
    os.mkdir('dataset/labels')
    os.mkdir('dataset/labels/train')
    os.mkdir('dataset/labels/val')

TRAIN_IMAGES = 'dataset/images/train'
VAL_IMAGES = 'dataset/images/val'
TRAIN_LABELS = 'dataset/labels/train'
VAL_LABELS = 'dataset/labels/val'

counter = 0

for label in os.listdir(THE_PATH):
    if label.endswith('.txt'):

        try:
            image = label.replace('.txt', '.jpeg')
            
            label_path = os.path.join(THE_PATH, label)
            image_path = os.path.join(THE_PATH, image)
            
            train_image_path = os.path.join(TRAIN_IMAGES, image)
            train_label_path = os.path.join(TRAIN_LABELS, label)

            val_image_path = os.path.join(VAL_IMAGES, image)
            val_label_path = os.path.join(VAL_LABELS, label)

            if counter < INTERVAL:
                os.system(f"mv {label_path} {train_label_path}")
                os.system(f"mv {image_path} {train_image_path}")
                counter += 1
            
            else:
                os.system(f"scp -r {label_path} {val_label_path}")
                os.system(f"scp -r {image_path} {val_image_path}")
                counter = 0
        except Exception as e:
            print(f"An exception occured in file: {label}. The exception is: {e}")
print("DONE!")

