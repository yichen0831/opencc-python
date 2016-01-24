#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import unittest


class OpenCCTest(unittest.TestCase):

    def setUp(self):
        self.openCC = OpenCC()

    def test_hk2s(self):
        self.openCC.set_conversion('hk2s')
        words = '香煙（英語：Cigarette），為煙草製品的一種。滑鼠是一種很常見及常用的電腦輸入設備。'
        self.assertEqual(self.openCC.convert(words), '香烟（英语：Cigarette），为烟草制品的一种。滑鼠是一种很常见及常用的电脑输入设备。')

    def test_s2hk(self):
        self.openCC.set_conversion('s2hk')
        words = '香烟（英语：Cigarette），为烟草制品的一种。鼠标是一种很常见及常用的电脑输入设备。'
        self.assertEqual(self.openCC.convert(words), '香煙（英語：Cigarette），為煙草製品的一種。鼠標是一種很常見及常用的電腦輸入設備。')

    def test_s2t(self):
        self.openCC.set_conversion('s2t')
        words = '香烟（英语：Cigarette），为烟草制品的一种。鼠标是一种很常见及常用的电脑输入设备。'
        self.assertEqual(self.openCC.convert(words), '香菸（英語：Cigarette），爲菸草製品的一種。鼠標是一種很常見及常用的電腦輸入設備。')

    def test_s2tw(self):
        self.openCC.set_conversion('s2tw')
        words = '香烟（英语：Cigarette），为烟草制品的一种。鼠标是一种很常见及常用的电脑输入设备。'
        self.assertEqual(self.openCC.convert(words), '香菸（英語：Cigarette），為菸草製品的一種。鼠標是一種很常見及常用的電腦輸入設備。')

    def test_s2twp(self):
        self.openCC.set_conversion('s2twp')
        words = '香烟（英语：Cigarette），为烟草制品的一种。內存是一种很常见及常用的电脑输入设备。'
        self.assertEqual(self.openCC.convert(words), '香菸（英語：Cigarette），為菸草製品的一種。記憶體是一種很常見及常用的電腦輸入裝置。')

    def test_t2hk(self):
        self.openCC.set_conversion('t2hk')
        words = '香菸（英語：Cigarette），爲菸草製品的一種。滑鼠是一種很常見及常用的電腦輸入裝置。'
        self.assertEqual(self.openCC.convert(words), '香煙（英語：Cigarette），為煙草製品的一種。滑鼠是一種很常見及常用的電腦輸入裝置。')

    def test_t2s(self):
        self.openCC.set_conversion('t2s')
        words = '香菸（英語：Cigarette），爲菸草製品的一種。滑鼠是一種很常見及常用的電腦輸入裝置。'
        self.assertEqual(self.openCC.convert(words), '香烟（英语：Cigarette），为烟草制品的一种。滑鼠是一种很常见及常用的电脑输入装置。')

    def test_t2tw(self):
        self.openCC.set_conversion('t2tw')
        words = '香菸（英語：Cigarette），爲菸草製品的一種。鼠標是一種很常見及常用的電腦輸入設備。'
        self.assertEqual(self.openCC.convert(words), '香菸（英語：Cigarette），為菸草製品的一種。鼠標是一種很常見及常用的電腦輸入設備。')

    def test_tw2s(self):
        self.openCC.set_conversion('tw2s')
        words = '香菸（英語：Cigarette），為菸草製品的一種。滑鼠是一種很常見及常用的電腦輸入裝置。'
        self.assertEqual(self.openCC.convert(words), '香烟（英语：Cigarette），为烟草制品的一种。滑鼠是一种很常见及常用的电脑输入装置。')

    def test_tw2sp(self):
        self.openCC.set_conversion('tw2sp')
        words = '香菸（英語：Cigarette），為菸草製品的一種。記憶體是一種很常見及常用的電腦輸入裝置。'
        self.assertEqual(self.openCC.convert(words), '香烟（英语：Cigarette），为烟草制品的一种。内存是一种很常见及常用的电脑输入设备。')


if __name__ == '__main__':
    sys.path.append(os.pardir)
    from opencc import OpenCC
    unittest.main()
