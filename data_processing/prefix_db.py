import json

# открываем файл для чтения и копируем в список
with open(file='../txt/prefix_id.txt', mode='r', encoding='utf-8') as f:
    prefix_ids = f.read().splitlines()


prefixes = []

for pref in prefix_ids:
    dict = {}
    dict['id'] = pref.split('.')[0].strip()
    dict['female_name'] = pref.split('.')[-1]
    dict['male_name'] = pref.split('.')[-1]
    if dict['female_name'] == 'Сибирская':
        dict['male_name'] = 'Сибирский'
    prefixes.append(dict)

    print(dict)

# сохраняем в json
with open('../result/prefix_result.json', 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(prefixes, ensure_ascii=False))
