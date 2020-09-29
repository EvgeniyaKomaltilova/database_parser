import json

# открываем исходный файл
with open(file='../raw_files/rats.json', mode='r', encoding='utf-8') as f:
    data = json.load(f)
# пустые списки для владельцев и заводчиков, будут использованы для получения списка персон
    breeders = []
    owners = []

# получение списка всех (уникальных) персон для дальнейшего исправления
for item in data:
    breeders.append(item['breeder_info'])
    owners.append(item['owner_info'])
persons = breeders + owners
unique_person_list = list(set(persons))

# приведение списка к одному формату (Фамилия И.О.|Локация)
splited_person = []
for person in unique_person_list:
    prsn = person.split(',')[0]
    city = person.split('.')[-1].split(',')[-1].split('(')[0].split(')')[0]
    splited_person.append(f"{prsn.split('(')[0]}|{city.strip()}")

# сортировка по списку и еще одна уникализация
splited_person_sorted = sorted(list(set(splited_person)))

# запись в текстовый файл
with open(file='../txt/persons_raw.txt', mode='w', encoding='utf-8') as f:
    for person in splited_person_sorted:
        f.write(f'{person}\n')
