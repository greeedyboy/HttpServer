import json,os

def load_sets():
    CONF_FILE = 'spiderset.json'
    #当前目录绝对路径
    work_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(work_dir)
    # print(work_dir)

    with open(CONF_FILE, 'r', encoding='utf-8') as b_oj:
        settings = json.load(b_oj)
    return settings