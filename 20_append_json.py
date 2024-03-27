import json
import numpy as np
from datetime import datetime

while True:
    random_number = np.random.randint(0, 10000)
    the_array = np.array([random_number, random_number + 1, random_number + 2, random_number + 3])
    
    the_list = the_array.tolist()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data_dict = {"timestamp": timestamp, "data": the_list}

    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(data_dict)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)