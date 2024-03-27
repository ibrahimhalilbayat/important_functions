from ultralytics import YOLO
import cv2
from ultralytics.yolo.utils.plotting import Annotator
import os

WEIGHT_PATH = 'rivendell' 
os.mkdir('detect')
DESTINATION = 'detect/'

model = YOLO(WEIGHT_PATH)

class_names_list = ['elf', 'man', 'dwarf', 'orc', 'goblin', 'uruk-hai']


cap = cv2.VideoCapture('test_video_2.mp4')

def main():
    id = 0
    while True:

        ret, frame = cv2.VideoCapture(0)
        image_name = str(id) + '.jpeg'
        cv2.imwrite(DESTINATION + image_name, frame, cv2.COLOR_BGR2RGB)
        txt_name = str(id) + '.txt'
        results = model.predict(frame)
        predictions = []

        for r in results:
            annotator = Annotator(frame)
            boxes = r.boxes
            for box in boxes:
                b = box.xywhn[0]
                c = box.cls
                predictions.append([int(c[0].item()), b[0].item(), b[1].item(), b[2].item(), 
                                        b[3].item()])
                annotator.box_label(b, model.names[int(c)])

        with open('detect/'+txt_name, "w") as file:
            for item in predictions:
                for inside_item in item:
                    file.write(str(inside_item) + " ")
                file.write("\n")

if __name__ == "__main__":
    main()
