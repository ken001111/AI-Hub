import os
import json
import shutil

source_directory = '/기존/디렉터리'  
target_directory = '/새로운/디렉터리'

if not os.path.exists(target_directory):
    os.makedirs(target_directory)

files_with_different_values = []
abnormal_numbering = []

json_list = os.listdir(source_directory)
json_files = [file for file in json_list if file.endswith('.json')]

for json_file in json_files:
    json_path = os.path.join(source_directory, json_file)
    with open(json_path,'r') as file:
        json_data = json.load(file)
        if all(json_data.get(key) == 3 for key in ['L1-L2', 'L2-L3', 'L3-L4', 'L4-L5', 'L5-S1', 'L1-L2disc', 'L2-L3disc', 'L3-L4disc','L4-L5disc','L5-S1disc']):
            continue 
        else:
            files_with_different_values.append(json_file)
            break

print("Files with at least one key having a value different than 3:", files_with_different_values)

for json_file in files_with_different_values:
    json_path = os.path.join(source_directory, json_file)
    with open(json_path, 'r') as file:
        json_data = json.load(file)
        for key in ['L1-L2', 'L2-L3', 'L3-L4', 'L4-L5', 'L5-S1', 'L1-L2disc', 'L2-L3disc', 'L3-L4disc','L4-L5disc','L5-S1disc']:
            value = json_data.get(key)
            if value in [4, 5, 6]:
                json_data[key] = 1
            elif value > 6:
                    abnormal_numbering.append(json_file)

        # 변경된 데이터를 복사하여 새로운 디렉터리에 파일로 저장
    with open(target_directory, 'w') as file:
        json.dump(json_data, file, indent=4)


