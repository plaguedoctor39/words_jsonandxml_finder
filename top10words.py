import json
import xml.etree.ElementTree as ET
from pprint import pprint
from collections import Counter


def words_json_finder(data):
    all_words = []
    for description_text in data['rss']['channel']['items']:
        # print(description_text['description'])
        all_words.extend(description_text['description'].split())
    all_words = sorted(all_words)
    all_words_sorted = list(filter(lambda x: len(x) > 6, all_words))
    all_words_sorted = Counter(all_words_sorted).most_common(10)
    return all_words_sorted


def words_xml_finder(file_path):
    tree = ET.parse(file_path)
    channel = tree.find('channel')
    item = channel.findall('item')
    all_words = []
    for description in item:
        desc = description.find('description')
        all_words.extend(desc.text.split())
    all_words = sorted(all_words)
    all_words_sorted = list(filter(lambda x: len(x) > 6, all_words))
    all_words_sorted = Counter(all_words_sorted).most_common(10)
    return all_words_sorted


def runner():
    with open('newsafr.json') as africa_file:
        data = json.load(africa_file)
        # pprint(data['rss']['channel']['items'])
        print('Для файла в формате .json\n', words_json_finder(data))

    print('Для файла в формате .xml\n', words_xml_finder('newsafr.xml'))


runner()
