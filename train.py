import json
import pandas as pd
import os
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
labels_list = list(set(labels_name))
# ['B-NAME_STUDENT', 'I-STREET_ADDRESS', 'B-EMAIL', 'B-URL_PERSONAL', 'I-NAME_STUDENT', 'B-PHONE_NUM', 'I-URL_PERSONAL', 'I-PHONE_NUM', 'B-USERNAME', 'B-STREET_ADDRESS', 'I-ID_NUM', 'B-ID_NUM'] 

# B-URL_PERSONAL 데이터와 토큰들 출력
label_list = {}
count_x = 0
for i in train['labels']:
    count_y = 0
    for r in i:
        if r != 'O' and r == 'B-URL_PERSONAL':
            print(r)
            print(train['tokens'][count_x][count_y])
        count_y += 1
    count_x+=1

# 데이터를 보면 B-URL_PERSONAL은 www가 포함하는것을 확인할 수 있다.
if re.search('www', token_data):
    label = 'B-URL_PERSONAL'
# B-EMAIL의 경우 '@'가 포함된다
elif re.serach('@', token_data):
    label = 'B-EMAIL'
# B-ID의 경우 숫자 12자리, '**:숫자 12자리', 