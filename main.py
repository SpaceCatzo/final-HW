import sys
import pandas as pd
from pathlib import Path


def main():
    string_path = get_path()
    file = load_csv(string_path)
    parsed_file = parse_content(file)
    changed_data = transform_data(parsed_file)
    create_txt(changed_data, string_path)
    print('Ура, получилось!')


def get_path():
    str_path = input('Укажите путь к csv файлу на Вашем компьютере (новый файл будет сохранен в этой же директории): ')
    return str_path.replace('"', '')


def load_csv(str_path):
    main_path = Path(str_path)
    try:
        file = pd.read_csv(main_path)
        return file
    except FileNotFoundError as e:
        print('Неправильный путь файла! Попытайтесь еще разочек...')
        sys.exit(1)


def parse_content(content):
    parsed_data = []
    for index, row in content.iterrows():
        name = row['name']
        device_type = row['device_type']
        browser = row['browser']
        sex = row['sex']
        age = row['age']
        bill = row['bill']
        region = row['region']

        parsed_data.append({
            'name': name,
            'device_type': device_type,
            'browser': browser,
            'sex': sex,
            'age': str(age)[0:-2],
            'bill': bill,
            'region': region
        })
    return parsed_data


def transform_data(parsed_data):
    for i in parsed_data:

        if i['sex'] == 'female':
            i['sex'] = 'женского'
            i['word'] = 'совершила'
        else:
            i['sex'] = 'мужского'
            i['word'] = 'совершил'

        match i['device_type']:
            case 'mobile':
                i['device_type'] = 'с мобильного телефона'
            case 'tablet':
                i['device_type'] = 'с планшета'
            case 'laptop':
                i['device_type'] = 'с ноутбука'
            case 'desktop':
                i['device_type'] = 'со стационарного компьютера'

        if i['region'] == '-':
            i['region'] = 'Нет информации'

        years_word_type_2 = ['2', '3', '4']
        years_word_type_1 = ['1']
        if i['age'][-1] in years_word_type_1:
            i['age_word'] = 'год'
        elif i['age'][-1] in years_word_type_2:
            i['age_word'] = 'года'
        else:
            i['age_word'] = 'лет'

    return parsed_data


def create_txt(transformed_data, str_path):
    new_path = Path(f'{str_path[0:-3]}txt')

    with open(new_path, 'w') as file:
        for i in transformed_data:
            file.write(
                f" • Пользователь {i['name']} {i['sex']} пола, {i['age']} {i['age_word']} {i['word']} покупку на {i['bill']} у.е. {i['device_type']} с помощью браузера {i['browser']}. Регион, из которого совершалась покупка: {i['region']}. \n")


main()
