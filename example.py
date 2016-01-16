#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from opencc import OpenCC


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        print('Require Python3 to run')
        sys.exit(0)

    openCC = OpenCC()
    openCC.set_conversion('s2twp')
    # openCC = OpenCC('s2twp')

    words = '鼠标是一种很常見及常用的電腦输入设备，它可以对当前屏幕上的游标进行定位，并通过按键和滚轮装置对游标所经过位置的' \
            '屏幕元素进行操作。鼠标的鼻祖於1968年出现。美国科学家道格拉斯·恩格尔巴特（Douglas Englebart）在加利福尼亚制作了' \
            '第一只鼠标。'

    result = openCC.convert(words)
    print("{} \n\n==> \n\n{}".format(words, result))
