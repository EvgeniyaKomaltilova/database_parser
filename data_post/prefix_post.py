import json
import requests


def prefix_post(path):
    url = f'{path}prefix/'

    with open(file='../result/prefix_result.json', mode='r', encoding='utf-8') as f:
        dicts = json.load(f)

        for dict in dicts:
            x = requests.post(url, data=dict)

            print(x.text)

