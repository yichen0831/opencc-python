from __future__ import print_function

import argparse
import sys
from opencc import OpenCC


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', metavar='<file>',
                        help='Read original text from <file>.')
    parser.add_argument('-o', '--output', metavar='<file>',
                        help='Write converted text to <file>.')
    parser.add_argument('-c', '--config', metavar='<file>',
                        help='Configuration file')
    args = parser.parse_args()

    if args.config is None:
        print("Please specify a configuration file.", file=sys.stderr)
        return 1

    cc = OpenCC(args.config)

    if args.input is not None:
        with open(args.input) as f:
            input_str = f.read()
    else:
        input_str = sys.stdin.read()

    output_str = cc.convert(input_str)

    if args.output is not None:
        with open(args.output, 'w') as f:
            f.write(output_str)
    else:
        sys.stdout.write(output_str)

    return 0


if __name__ == '__main__':
    sys.exit(main())
