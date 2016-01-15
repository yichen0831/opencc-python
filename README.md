# opencc-python 開放中文轉換 Python

## OpenCC made with Python

## Introduction 簡介
opencc-python is made by Python with the dictionary files of [OpenCC](https://github.com/BYVoid/OpenCC) which is developed by BYVoid(<byvoid.kcp@gmail.com>).

opencc-python是用Python所寫, 使用由BYVoid(<byvoid.kcp@gmail.com>)所開發的[OpenCC](https://github.com/BYVoid/OpenCC)中的字典檔案.

opencc-python can run with Python2.7 and Python3.x

opencc-python可以支援Python2.7及Python3.x


## Installation 安裝
Just copy the opencc folder to the project you are developing.

把opencc這個目錄複製到你正在開發的專案中即可.

Or run (require administration privilege)或是執行(需要管理者權限):

    python setup.py install


## Usage 使用方式

    from opencc import OpenCC 
    
    openCC = OpenCC('s2t')  # convert from Simplified Chinese to Traditional Chinese
    # can also set conversion by calling set_conversion
    # openCC.set_conversion('s2tw')
    to_convert = '开放中文转换'
    converted = openCC.convert(to_convert)

Conversions include 轉換包含:

'hk2s': Traditional Chinese (Hong Kong standard) to Simplified Chinese

's2hk': Simplified Chinese to Traditional Chinese (Hong Kong standard)

's2t': Simplified Chinese to Traditional Chinese

's2tw': Simplified Chinese to Traditional Chinese (Taiwan standard)

's2twp': Simplified Chinese to Traditional Chinese (Taiwan standard, with phrases)

't2hk': Traditional Chinese to Traditional Chinese (Hong Kong standard)

't2s': Traditional Chinese to Simplified Chinese

't2tw': Traditional Chinese to Traditional Chinese (Taiwan standard)

'tw2s': Traditional Chinese (Taiwan standard) to Simplified Chinese

'tw2sp': Traditional Chinese (Taiwan standard) to Simplified Chinese (with phrases)

## Issues 問題
When there are more than one conversion avaiable, only the first one is taken.

當轉換有兩個以上的字詞可能時, 程式只會使用第一個.
