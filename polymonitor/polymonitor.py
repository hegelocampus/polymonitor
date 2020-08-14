#!/usr/bin/env python3
import argparse as ap


def main():
    description = 'Displays site status for polybar.'
    parser = ap.ArgumentParser(description)
    parser.add_argument(
        '-s',
        '--symbolic',
        help='Displays the results as symbols',
        action='store_true')
    parser.add_argument(
        '-t',
        '--text',
        help='Displays the results as readable text',
        action='store_true')
    parser.add_argument(
        '-c',
        '--compact',
        help='Reduces the results into a more compact package',
        action='store_true')
    parser.add_argument(
        '-u',
        '--urls',
        help='Pass in URLs to monitor',
        action='extend')

    args = parser.parse_args()

    # res = ""
    print(args)


if __name__ == '__main__':
    main()
