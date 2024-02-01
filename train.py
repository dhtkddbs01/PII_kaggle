import json
import pandas as pd
impo
SYS_INPUT_DIR = '/kaggle/input/pii-detection-removal-from-educational-data'
train_json = json.load(open(os.path.join(SYS_INPUT_DIR, "train.json")))
# json 파일 데이터 프레임으로 변환하기.
train = pd.json_normalize(train_json)
train.head()

# 라벨링 데이터가 무엇인지 찾기
labels_name = []
for i in train['labels']:
    for r in i:
        if r != 'O':
            labels_name.append(r)
# set으로 변환하여 중복 제거            
labels_name = set(labels_name)
# set으로 변환한 자료 다시 리스트로 변환
labels_name_list = list(set(labels_name))
# ['B-NAME_STUDENT', 'I-STREET_ADDRESS', 'B-EMAIL', 'B-URL_PERSONAL', 'I-NAME_STUDENT', 'B-PHONE_NUM', 'I-URL_PERSONAL', 'I-PHONE_NUM', 'B-USERNAME', 'B-STREET_ADDRESS', 'I-ID_NUM', 'B-ID_NUM'] 