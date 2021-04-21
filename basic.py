from classes import *

def get_data(files):
    result = list() #список, в котором будет храниться результат
    
    #формирование списка общих ключей (названия столбцов), "пересечение" списков
    keys = set(files[0].keys)
    for f in files:
        keys &= set(f.keys)
    
    #нормализация данных, то есть отбор тех, которые подходят по названию столбца
    for f in files:
        f.normalize(sorted(keys))
        result += f.data
    
    #сортировка результата по 'D1' 
    #в случае, если необходима сортировка по нескольким столбцам, 
    #необходимо создать кортеж из этих столбцов
    return sorted(result, key=lambda k: k['D1'])

#функция записи результата в файл
def write_data(data, file_name):
    with open(file_name, 'w') as output_file:
        writer = csv.writer(output_file, delimiter='\t')
        writer.writerow(data[0].keys())
        for row in data:
            writer.writerow(row.values())

if __name__ == '__main__':
    import csv
    files = [CSV('csv_data_1.csv'),
            CSV('csv_data_2.csv'),
            XML('xml_data.xml'),
            JSON('json_data.json')]
            
    result = get_data(files)
    write_data(result, 'basic_results.tsv')
