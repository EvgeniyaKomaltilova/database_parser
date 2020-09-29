import json
import requests


def rats_put(path):
    with open(file='../result/rats_litters.json', mode='r', encoding='utf-8') as f:
        dicts = json.load(f)

        for dict in dicts:
            url = f'{path}rats/{dict["id"]}/'
            x = requests.patch(url, data={'litter': dict['litter']})

            print(x.text)

