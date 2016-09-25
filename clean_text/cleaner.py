# -*- coding: utf-8 -*-

import os
import nltk
import codecs
from nltk.tag import pos_tag

# from pyth.plugins.rtf15.reader import Rtf15Reader
# from pyth.plugins.plaintext.writer import PlaintextWriter

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rename_file(filename=basestring):
    new_name = filename.replace(os.sep, '_')[:-4]
    return ROOT_DIR + os.sep + new_name + '.txt'


def get_files(path=basestring):
    if not os.path.isdir(path):
        raise IOError('Object {0} is not a folder'.format(path))
    for dirpath, dirnames, filenames in os.walk(path):
        for file_ in filenames:
            if file_.endswith('.txt') or file_.endswith('.rtf'):
                yield os.path.join(dirpath, file_)


def read_and_process_file(filename=basestring, output_file=None):
    with open(filename, 'rb') as r:
        text = r.read().decode(encoding='utf-8', errors='ignore')
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(text)
    if not output_file:
        output_file = filename
    output_file = rename_file(output_file)
    with open(output_file, 'wb') as w:
        for sentence in sentences:
            tagged_sent = pos_tag(sentence.split())
            if not [word for word, pos in tagged_sent if pos == 'NNP']:
                w.write(sentence)


def clean_text(filename_or_folder=basestring, output_file=None):
    if os.path.isfile(filename_or_folder):
        read_and_process_file(filename_or_folder, output_file)
    elif os.path.isdir(filename_or_folder):
        for file_ in get_files(filename_or_folder):
            read_and_process_file(file_, output_file)
    else:
        raise IOError('Cannot get access to {0} object'.format(filename_or_folder))
