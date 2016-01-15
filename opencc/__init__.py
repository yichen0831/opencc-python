##########################################################
# Author: Yichen Huang (Eugene)
# GitHub: https://github.com/yichen0831/opencc-python
# January, 2016
##########################################################

import os
import json

CONFIG_DIR = 'config'
DICT_DIR = 'dictionary'


class OpenCC:
    def __init__(self, conversion=None):
        """
        init OpenCC
        :param conversion: the conversion of usage, options are
         'hk2s', 's2hk', 's2t', 's2tw', 's2twp', 't2hk', 't2s', 't2tw', 'tw2s', and 'tw2sp'
         check the json file names in config directory
        :return: None
        """
        self.conversion_name = ''
        self.conversion = conversion
        self._dict_init_done = False
        self._dict_chain = list()
        self._dict_chain_data = list()
        if self.conversion is not None:
            self._init_dict()

    def convert(self, string):
        """
        convert string from Simplified Chinese to Traditional Chinese or vice versa
        :param string: the input string
        :return: converted string
        """
        if not self._dict_init_done:
            self._init_dict()
            self._dict_init_done = True

        converted_string = string
        converted_string_list = list(converted_string)
        for c_dict in self._dict_chain_data:
            for key in c_dict:
                pos = 0
                while pos < len(converted_string):
                    index = converted_string.find(key, pos)
                    if index == -1:
                        break

                    value = c_dict[key]

                    if len(value.split(' ')) > 1:
                        # multiple mapping, use the first one for now
                        value = value.split(' ')[0]

                    converted_string_list[index:index+len(key)] = list(value)
                    if len(key) != len(value):
                        converted_string = ''.join(converted_string_list)
                    pos = index + len(value)
            converted_string = ''.join(converted_string_list)

        return converted_string

    def _init_dict(self):
        """
        init the dict with conversion
        :return: None
        """
        if self.conversion is None:
            raise ValueError('conversion is not set')

        self._dict_chain = []
        config = self.conversion + '.json'
        config_file = os.path.join(os.path.dirname(__file__), CONFIG_DIR, config)
        with open(config_file) as f:
            setting_json = json.load(f)

        self.conversion_name = setting_json.get('name')

        for chain in setting_json.get('conversion_chain'):
            self._add_dict_chain(self._dict_chain, chain.get('dict'))

        self._dict_chain_data = []
        for filename in self._dict_chain:
            map_dict = {}
            with open(filename) as f:
                for line in f:
                    key, value = line.strip().split('\t')
                    map_dict[key] = value
            self._dict_chain_data.append(map_dict)

        self._dict_init_done = True

    def _add_dict_chain(self, dict_chain, dict_dict):
        """
        add dict chain
        :param dict_chain: the dict chain to add
        :param dict_dict: the dict to be added in
        :return: None
        """
        if dict_dict.get('type') == 'group':
            for dict_item in dict_dict.get('dicts'):
                self._add_dict_chain(dict_chain, dict_item)
        elif dict_dict.get('type') == 'txt':
            filename = dict_dict.get('file')
            dict_file = os.path.join(os.path.dirname(__file__), DICT_DIR, filename)
            dict_chain.append(dict_file)

    def set_conversion(self, conversion):
        """
        set conversion
        :param conversion: the conversion of usage, options are
         'hk2s', 's2hk', 's2t', 's2tw', 's2twp', 't2hk', 't2s', 't2tw', 'tw2s', and 'tw2sp'
         check the json file names in config directory
        :return: None
        """
        if self.conversion == conversion:
            return
        else:
            self._dict_init_done = False
            self.conversion = conversion

