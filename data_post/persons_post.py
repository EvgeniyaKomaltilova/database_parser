import json
import requests


def persons_post(path):
    url = f'{path}persons/'

    with open(file='../result/persons_result.json', mode='r', encoding='utf-8') as f:
        dicts = json.load(f)

        for dict in dicts:
            x = requests.post(url, data=dict)

            print(x.text)

