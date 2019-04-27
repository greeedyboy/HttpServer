import json,os

def load_sets():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    # print('当前目录绝对路径:', dir_path)
    settingfile =dir_path+ '\spiderset.json'
    with open(settingfile, 'r', encoding='utf-8') as b_oj:
        settings = json.load(b_oj)
    # print(settings)
    return settings
#获取当前目录绝对路径
