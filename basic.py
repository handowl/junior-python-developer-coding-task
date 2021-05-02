from classes import CSV, XML, JSON
import os
import csv

def get_data(file_names):
    result = list() #список, в котором будет храниться результат
    
    files = list()
    class_dict = {'csv': CSV, 'xml': XML, 'json':JSON}
    for file_name in file_names:
        extension = file_name.split('.')[-1]
        file_path = os.path.join('input_data', file_name)
        files.append(class_dict[extension](file_path))
    for file in files:
        file.read()
    
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
    input_file_names = os.listdir('input_data')
    result = get_data(input_file_names)
    write_data(result, os.path.join('output_data', 'basic_results.tsv'))
