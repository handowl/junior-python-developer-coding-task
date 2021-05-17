import csv
import json
import xml.etree.ElementTree as ET


#родительский класс
class Default: 

    def __init__(self, file_name):
        self.file_name = file_name
        
        self.data = list() #список словарей {столбец: значение, ...}
        self.keys = list() #список только ключей, то есть только столбцов
    
    #функция, отбирающая только нужные столбцы и их значения
    def normalize(self, keys_list):
        new_data = list()
        for row in self.data:
            new_row = {key:str(row[key]) for key in keys_list}
            new_data.append(new_row)
        self.data = new_data
        
    def read(self):
        pass       

#класс данных из CSV-файла
class CSV(Default):
        
    def read(self):
        with open(self.file_name) as csv_file:
            reader = csv.DictReader(csv_file)
            self.data = [i for i in reader]
            self.keys = list(self.data[0].keys())

#класс данных из XML-файла
class XML(Default):
    def read(self):
        xml_tree = ET.parse(self.file_name)
        root = xml_tree.getroot()
        for obj in root.iter('objects'):
            obj_data = dict()
            for field in obj.iter('object'):
                key = list(field.attrib.values())[0]
                value = list(field.iter('value'))[0].text
                obj_data[key] = value
            self.data.append(obj_data)
        self.keys = list(self.data[0].keys())

#класс данных из JSON-файла
class JSON(Default):
    def read(self):
        with open(self.file_name) as json_file:
            reader = json.load(json_file)
            self.data = [i for i in reader['fields']]
            self.keys = list(self.data[0].keys())

