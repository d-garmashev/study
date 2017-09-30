# coding: utf-8

import json
import chardet


def file_to_json(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        encoding_result = chardet.detect(data)['encoding']
    data_json = json.loads(data.decode(encoding_result))
    return data_json


def merge_texts_split_by_words(input_json):
    result = []
    for text in input_json['rss']['channel']['items']:
        result += text['description'].lower().split(' ')
    return result


def top_n_words_count(input_list, n):
    word_counter = {}
    for word in set(input_list):
        if len(word) > 6:
            word_counter[word] = input_list.count(word)
    result = sorted(word_counter, key=word_counter.get, reverse=True)[:n]
    return result


def print_result(filename, n):
    data_json = file_to_json(filename)
    data_list = merge_texts_split_by_words(data_json)
    top_n_words = top_n_words_count(data_list, n)
    print(filename, ':', top_n_words)


filename_list = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
words_num = 10

print(' '.join(['Top ', str(words_num), 'words for texts']))
for file in filename_list:
    print_result(file, words_num)