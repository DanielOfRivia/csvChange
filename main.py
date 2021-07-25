import csv


def read_file(file_name):
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        names = []
        dates = []
        for table in reader:
            names.append(table[0])
            dates.append(table[1])
            print(table)
        names_set = set(names)
        dates_set = set(dates)

    # with open('result.csv', 'w', newline='') as new_file:
    #     writer = csv.writer(new_file)


# def change_date(date_text):


read_file('addresses.csv')
