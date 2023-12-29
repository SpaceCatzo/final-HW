from pathlib import Path
import pandas as pd


def main():
    file = load_csv()
    parsed_file = parse_content(file)
    changed_data = transform_data(parsed_file)
    write_lines(changed_data)


def load_csv():
    str_path = input('Укажите путь к csv файлу на Вашем компьютере: ')
    main_path = Path(str_path.replace('"', ''))
    return pd.read_csv(main_path)


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
            'age': int(age),
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

    return parsed_data


def write_lines(transformed_data):
    for i in transformed_data:
        print(
            f"Пользователь {i['name']} {i['sex']} пола, {i['age']} лет {i['word']} покупку на {i['bill']} у.е. {i['device_type']} с помощью браузера {i['browser']}. Регион, из которого совершалась покупка: {i['region']}. ")


main()
