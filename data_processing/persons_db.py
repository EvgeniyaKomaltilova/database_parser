import json

# открываем файл для чтения и копируем в список
with open(file='txt/persons.txt', mode='r', encoding='utf-8') as f:
    persons = f.read().splitlines()

# список для словарей, который потом станет json'ом
person_dicts = []

# разбиваем строку на фамилию, имя, отчество и локацию
for i in range(1, len(persons)):
    dict = {}
    dict['id'] = i
    dict['last_name'] = persons[i].split(' ')[0].strip()
    dict['first_name'] = persons[i].split('.')[0].split(' ')[-1].strip()
    dict['second_name'] = persons[i].split('|')[0].split('.')[-1].strip()
    dict['location'] = persons[i].split('|')[-1].strip()
    person_dicts.append(dict)

# у кого нет отчечтва, тому None
for dict in person_dicts:
    if dict['second_name'] == '':
        dict['second_name'] = None

# меняем локацию на ID согласно location.txt
for dict in person_dicts:
    if dict['location'] == 'СПб' or dict['location'] == 'СПБ' or dict['location'] == 'г СПб' \
            or dict['location'] == 'Санкт-Петербург' or dict['location'] == 'ЛО':
        dict['location'] = 1
    elif dict['location'] == 'Москва' or dict['location'] == 'МО':
        dict['location'] = 2
    elif dict['location'] == 'Воронеж':
        dict['location'] = 3
    elif dict['location'] == 'Мурино':
        dict['location'] = 4
    elif dict['location'] == 'Минск':
        dict['location'] = 5
    elif dict['location'] == 'Ростов-на-Дону':
        dict['location'] = 6
    elif dict['location'] == 'Коммунар':
        dict['location'] = 7
    elif dict['location'] == 'Выборг':
        dict['location'] = 8
    elif dict['location'] == 'Нижний Новгород':
        dict['location'] = 9
    elif dict['location'] == 'Пушкин':
        dict['location'] = 10
    elif dict['location'] == 'Приморск':
        dict['location'] = 11
    elif dict['location'] == 'Новгород':
        dict['location'] = 12
    elif dict['location'] == 'Владимир':
        dict['location'] = 13
    elif dict['location'] == 'Кудрово':
        dict['location'] = 14
    elif dict['location'] == 'Колпино':
        dict['location'] = 15
    elif dict['location'] == 'Туапсе':
        dict['location'] = 16
    elif dict['location'] == 'Сиверский':
        dict['location'] = 17
    elif dict['location'] == 'Усмань':
        dict['location'] = 18
    elif dict['location'] == 'Брест':
        dict['location'] = 19
    elif dict['location'] == 'Боровичи':
        dict['location'] = 20
    elif dict['location'] == 'Волгоград':
        dict['location'] = 21
    elif dict['location'] == 'Кингисепп':
        dict['location'] = 22
    elif dict['location'] == 'Омск':
        dict['location'] = 23
    elif dict['location'] == 'Екатеринбург':
        dict['location'] = 24
    elif dict['location'] == 'Одинцово':
        dict['location'] = 25
    elif dict['location'] == 'Самара':
        dict['location'] = 26
    elif dict['location'] == 'Удомля':
        dict['location'] = 27
    elif dict['location'] == 'Всеволожск':
        dict['location'] = 28
    elif dict['location'] == 'Архангельск':
        dict['location'] = 29
    elif dict['location'] == 'Апатиты':
        dict['location'] = 30
    elif dict['location'] == 'Донецк':
        dict['location'] = 31
    elif dict['location'] == 'Калуга':
        dict['location'] = 32
    elif dict['location'] == 'Томск':
        dict['location'] = 33
    elif dict['location'] == 'Кировск':
        dict['location'] = 34
    elif dict['location'] == 'Новосибирск':
        dict['location'] = 35
    elif dict['location'] == 'Белгород':
        dict['location'] = 36
    elif dict['location'] == 'Орел':
        dict['location'] = 37
    elif dict['location'] == 'Гатчина':
        dict['location'] = 38
    elif dict['location'] == 'Токсово':
        dict['location'] = 39
    elif dict['location'] == 'Шлиссельбург':
        dict['location'] = 40
    elif dict['location'] == 'Нефтюганск':
        dict['location'] = 41
    elif dict['location'] == 'Ярославль':
        dict['location'] = 42
    elif dict['location'] == 'Смоленск':
        dict['location'] = 43
    elif dict['location'] == 'Кронштадт':
        dict['location'] = 44
    elif dict['location'] == 'Финляндия':
        dict['location'] = 45

    print(dict)

# сохраняем в json
with open('../result/persons_result.json', 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(person_dicts, ensure_ascii=False))

