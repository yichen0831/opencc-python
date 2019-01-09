# 開放中文轉換（Pure Python）

Open chinese convert (OpenCC) in pure Python.

## Introduction 簡介

[opencc-python](https://github.com/yichen0831/opencc-python) 是用純 Python 所寫，使用由 BYVoid(<byvoid.kcp@gmail.com>) 所開發的 [OpenCC](https://github.com/BYVoid/OpenCC) 中的字典檔案。
opencc-python 可以支援 Python2.7 及 Python3.x。

[opencc-python](https://github.com/yichen0831/opencc-python) is made by pure Python with the dictionary files of [OpenCC](https://github.com/BYVoid/OpenCC) which is developed by BYVoid(<byvoid.kcp@gmail.com>).

opencc-python can run with Python2.7 and Python3.x.

## Installation 安裝

將 `opencc` 這個目錄複製到你正在開發的專案中即可，或是執行（需要管理者權限）：

```sh
python setup.py install
```

套件也可從 [PyPI](https://pypi.org/project/opencc-python-reimplemented/) 安裝，使用指令：

```sh
pip install opencc-python-reimplemented
```

Copy the `opencc` folder to the your project, or run (admin required)

```sh
python setup.py install
```

The package can also be instally from [PyPI](https://pypi.org/project/opencc-python-reimplemented/) by issuing:

```sh
pip install opencc-python-reimplemented
```

## Usage 使用方式
### Code

``` python
from opencc import OpenCC
cc = OpenCC('s2t')  # convert from Simplified Chinese to Traditional Chinese
# can also set conversion by calling set_conversion
# cc.set_conversion('s2tw')
to_convert = '开放中文转换'
converted = cc.convert(to_convert)
```
### Command Line

```sh
usage: python -m opencc [-h] [-i <file>] [-o <file>] [-c <conversion>]
                        [--in-enc <encoding>] [--out-enc <encoding>]

optional arguments:
  -h, --help            show this help message and exit
  -i <file>, --input <file>
                        Read original text from <file>. (default: None = STDIN)
  -o <file>, --output <file>
                        Write converted text to <file>. (default: None = STDOUT)
  -c <conversion>, --config <conversion>
                        Conversion (default: None)
  --in-enc <encoding>   Encoding for input (default: UTF-8)
  --out-enc <encoding>  Encoding for output (default: UTF-8)

example with UTF-8 encoded file:

  python -m opencc -c s2t -i my_simplified_input_file.txt -o my_traditional_output_file.txt

See https://docs.python.org/3/library/codecs.html#standard-encodings for list of encodings.
```

### Conversions 轉換

* `hk2s`: Traditional Chinese (Hong Kong standard) to Simplified Chinese

* `s2hk`: Simplified Chinese to Traditional Chinese (Hong Kong standard)

* `s2t`: Simplified Chinese to Traditional Chinese

* `s2tw`: Simplified Chinese to Traditional Chinese (Taiwan standard)

* `s2twp`: Simplified Chinese to Traditional Chinese (Taiwan standard, with phrases)

* `t2hk`: Traditional Chinese to Traditional Chinese (Hong Kong standard)

* `t2s`: Traditional Chinese to Simplified Chinese

* `t2tw`: Traditional Chinese to Traditional Chinese (Taiwan standard)

* `tw2s`: Traditional Chinese (Taiwan standard) to Simplified Chinese

* `tw2sp`: Traditional Chinese (Taiwan standard) to Simplified Chinese (with phrases)

## Issues 問題

當轉換有兩個以上的字詞可能時，程式只會使用第一個。

When there are more than one conversion available, only the first one is taken.
