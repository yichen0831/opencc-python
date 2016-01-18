from setuptools import setup, find_packages
from codecs import open
from os import path

cwd = path.abspath(path.dirname(__file__))

with open(path.join(cwd, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='opencc-python',
        version='0.1.0',
        description='OpenCC made with Python',
        long_description=long_description,
        url='https://github.com/yichen0831/opencc-python',
        author='Yichen Huang (Eugene)',
        author_email='yichen0831@gmail.com',
        license='Apache License',
        classifiers=[
            'Development Status :: 3 -Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Chinese Conversion',
            'License :: OSI Approved :: Apache License 2.0',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',

        ],
        keywords='chinese conversion',
        packages=['opencc'],
        install_requires=[],
        package_data={
            'opencc': [
                'LICENSE',
                'NOTICE.txt',
                'config/hk2s.json', 'config/s2hk.json', 'config/s2t.json',
                'config/s2tw.json', 'config/s2twp.json', 'config/t2hk.json',
                'config/t2s.json', 'config/t2tw.json', 'config/tw2s.json',
                'config/tw2sp.json',
                'dictionary/HKVariants.txt',
                'dictionary/HKVariantsPhrases.txt',
                'dictionary/HKVariantsRev.txt',
                'dictionary/HKVariantsRevPhrases.txt',
                'dictionary/JPVariants.txt',
                'dictionary/STCharacters.txt',
                'dictionary/STPhrases.txt',
                'dictionary/TSCharacters.txt',
                'dictionary/TSPhrases.txt',
                'dictionary/TWPhrases.txt',
                'dictionary/TWPhrasesRev.txt',
                'dictionary/TWVariants.txt',
                'dictionary/TWVariantsRev.txt',
                'dictionary/TWVariantsRevPhrases.txt',
            ]
        },
)
