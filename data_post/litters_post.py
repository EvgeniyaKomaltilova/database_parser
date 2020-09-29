import json
import requests


def litters_post(path):
    url = f'{path}litters/'

    with open(file='../result/litters_result.json', mode='r', encoding='utf-8') as f:
        dicts = json.load(f)

        for dict in dicts:
            x = requests.post(url, data=dict)

            print(x.text)

