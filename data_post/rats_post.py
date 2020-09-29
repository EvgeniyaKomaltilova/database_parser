import json
import requests


def rats_post(path):
    url = f'{path}rats/'

    with open(file='../result/rats_result_without_litters.json', mode='r', encoding='utf-8') as f:
        dicts = json.load(f)

        for dict in dicts:
            x = requests.post(url, data=dict)

            print(x.text)

