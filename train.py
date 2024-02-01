import json
import pandas as pd
import os

# os를 통해 kaggle train data 불러오기
SYS_INPUT_DIR = '/kaggle/input/pii-detection-removal-from-educational-data'
train_json = json.load(open(os.path.join(SYS_INPUT_DIR, "train.json")))
# json 파일 데이터 프레임으로 변환하기.
train = pd.json_normalize(train_json)

git