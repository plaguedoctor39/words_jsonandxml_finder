import json
import xml.etree.ElementTree as ET
from pprint import pprint
from collections import Counter
from pathlib import Path


def words_finder(file_path):
    all_words = []
    if Path(file_path).suffix == '.json':
        with open(file_path) as africa_file:
            data = json.load(africa_file)
        for description_text in data['rss']['channel']['items']:
            # print(description_text['description'])
            all_words.extend(description_text['description'].split())
    elif Path(file_path).suffix == '.xml':
        tree = ET.parse(file_path)
        channel = tree.find('channel')
        item = channel.findall('item')
        for description in item:
            desc = description.find('description')
            all_words.extend(desc.text.split())
    else:
        return f'Расширения {Path(file_path).suffix} не поддерживаются программой'
    all_words = [x.lower() for x in all_words]
    all_words = sorted(all_words)
    all_words_sorted = list(filter(lambda x: len(x) > 6, all_words))
    all_words_sorted = Counter(all_words_sorted).most_common(10)
    return all_words_sorted




def runner():
    with open('newsafr.json') as africa_file:
        data = json.load(africa_file)
        # pprint(data['rss']['channel']['items'])
        print('Для файла в формате .json\n', words_finder('newsafr.json'))

    print('Для файла в формате .xml\n', words_finder('newsafr.xml'))


runner()
