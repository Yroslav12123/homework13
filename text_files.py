import csv

with open('airport-codes_csv (1).csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')

    header = next(reader)
    try:
        name_index = header.index('name')
        iso_country_index = header.index('iso_country')
    except ValueError:
        print("Столбцы 'name' или 'iso_country' не найдены в заголовке.")
        exit()


    for row in reader:
        try:
            if row[iso_country_index] == 'UA':
                print(row[name_index])
        except IndexError:
            print(f"Пропущена некорректная строка: {row}")

