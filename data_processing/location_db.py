import json


# открываем файл для чтения и копируем в список
with open(file='../txt/location_id.txt', mode='r', encoding='utf-8') as f:
    locations = f.read().splitlines()

loc_result = []

for loc in locations:
    dict = {}
    dict['id'] = loc.split(' ')[0]
    dict['city'] = loc.split(' ')[-1]
    dict['country'] = 'Россия'
    if dict['city'] == 'Порвоо':
        dict['country'] = 'Финляндия'
    elif dict['city'] == 'Донецк':
        dict['country'] = 'Украина'
    elif dict['city'] == 'Брест' or dict['city'] == 'Минск':
        dict['country'] = 'Беларусь'
    loc_result.append(dict)

    print(dict)

# сохраняем в json
with open('../result/locations_result.json', 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(loc_result, ensure_ascii=False))
