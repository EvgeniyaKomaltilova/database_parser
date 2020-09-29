import json
import requests


def locations_post(path):
    url = f'{path}locations/'

    with open(file='../result/locations_result.json', mode='r', encoding='utf-8') as f:
        dicts = json.load(f)

        for dict in dicts:
            x = requests.post(url, data=dict)

            print(x.text)
