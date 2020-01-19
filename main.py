#! /usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import os

import requests
from bs4 import BeautifulSoup

from star_dict import StarDict


def phonetic_from_local(word_list: list) -> list:
    phonetic_list = []
    # From https://github.com/skywind3000/ECDICT/releases/download/1.0.28/ecdict-sqlite-28.zip
    with StarDict('dictionary/star_dict.db') as db:
        query_result = db.query_batch(word_list)
        for word in query_result:
            if word is None:
                phonetic_list.append('')
            else:
                phonetic_list.append(word['phonetic'])
    return phonetic_list


def phonetic_from_youdao(word_list: list) -> list:
    phonetic_list = []
    base_url = 'http://dict.youdao.com/w/'
    for word in word_list:
        response = requests.get(base_url + word)
        soup = BeautifulSoup(response.text, 'html.parser')
        response.close()

        pronounces = soup.select('span[class="phonetic"]')
        if pronounces is None or len(pronounces) == 0:
            phonetic_list.append('')
        else:
            phonetic_list.append(pronounces[0].text[1:-1])
    return phonetic_list


def phonetic_from_both(word_list: list) -> list:
    phonetic_list = phonetic_from_local(word_list)
    print('> Getting Phonetic From Offline Success')
    for index, (word, phonetic) in enumerate(zip(word_list, phonetic_list)):
        if phonetic == '':
            print('> Getting Unknown Phonetic From Online: ' + word)
            phonetic_list[index] = phonetic_from_youdao([word])[0]
    return phonetic_list


def translate_csv(file_path: str, output_path: str, phonetic_getter: callable):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)

        data = [words for words in reader]
        word_list = [items[0] for items in data]

        phonetic_list = phonetic_getter(word_list)
        lines = [[words[0], phonetic] for words, phonetic in zip(data, phonetic_list)]

    with open(output_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(lines)


if __name__ == '__main__':
    if os.path.exists('input'):
        if not os.path.exists('output'):
            os.mkdir('output')
        print('Work Start!')
        for root, dirs, files in os.walk('input'):
            for f in files:
                if not f.startswith('.'):
                    if f.endswith('.csv'):
                        print('\nFor File: ' + f)
                        translate_csv(os.path.join(root, f), os.path.join('output', f), phonetic_from_both)
                    else:
                        print('\n File \'' + f + '\' is not a csv!')
        print('\nAll Done!')
    else:
        os.mkdir('input')
        print('No Input!')
