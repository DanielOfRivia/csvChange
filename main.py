import csv


def process_file(file_name):
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        names = []
        dates = []
        dictionary = {}
        current_date = 0
        for table in reader:
            if current_date != table[1]:
                dictionary.update({change_date(table[1]): [[table[0], table[2]]]})
                if current_date != 0:
                    dictionary[change_date(current_date)].sort()
                current_date = table[1]
            else:
                dictionary[change_date(table[1])].append([table[0], table[2]])
            names.append(table[0])
            dates.append(change_date(table[1]))
        dictionary[change_date(current_date)].sort()
        names_set = set(names)
        dates_set = set(dates)
        dates_sorted = []
        names_sorted = []
        for d in dates_set:
            dates_sorted.append(d)
        dates_sorted.sort()
        for nam in names_set:
            names_sorted.append(nam)
        names_sorted.sort()
        final_arr = []
        for name in names_sorted:
            final_arr.append([name])
        for date in dates_sorted:
            ii = 0
            i = 0
            for n in names_sorted:
                if ii != len(dictionary[date]) and n == dictionary[date][ii][0]:
                    final_arr[i].append(dictionary[date][ii][1])
                    ii += 1
                else:
                    final_arr[i].append('0')
                i += 1
        dates_sorted.insert(0, 'Name/Date')
        final_arr.insert(0, dates_sorted)
    return final_arr


def write_file(changed_table):
    with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(changed_table)


def change_date(date_text):
    arr = date_text.split()
    return arr[2] + '-' + change_month(arr[0]) + '-' + arr[1]


def change_month(text):
    return {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12',
    }[text]


write_file(process_file('acme_worksheet.csv'))
