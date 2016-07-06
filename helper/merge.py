#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##########################################################
# Author: Yichen Huang (Eugene)
# GitHub: https://github.com/yichen0831/opencc-python
# January, 2016
##########################################################

import sys
import os

DICT_DIRECTORY = '../opencc/dictionary'

MER_INPUTS = [
    'TWPhrasesIT.txt',
    'TWPhrasesName.txt',
    'TWPhrasesOther.txt'
]

MER_OUTPUT = 'TWPhrases.txt'


def merge(mer_inputs=MER_INPUTS, mer_output=MER_OUTPUT):
    """
    merge the phrase files into one file
    :param mer_inputs: the phrase files
    :param mer_output: the output file
    :return: None
    """
    dirname = os.path.dirname(__file__)
    output_file = os.path.join(dirname, DICT_DIRECTORY, mer_output)
    lines = []
    for in_file in MER_INPUTS:
        input_file = os.path.join(dirname, DICT_DIRECTORY, in_file)
        with open(input_file, encoding='utf-8') as f:
            for line in f:
                lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        print('Requires Python3 to run')
        sys.exit(0)
    merge()
