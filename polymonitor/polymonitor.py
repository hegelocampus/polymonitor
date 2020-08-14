#!/usr/bin/env python3

import argparse as ap
from functools import reduce
from requests import get, codes
from requests.exceptions import MissingSchema


def make_value_dict(is_symbolic):
    map_to_res = {
        True: 'f062'.decode('hex') if is_symbolic else "Up",
        False: 'f98d'.decode('hex') if is_symbolic else "Down"
    }

    return map_to_res


def get_status_code(url):
    """
    Gets the current status code of a full url or short url. Short urls will
    be prepended with https.
    """
    try:
        return get(url).status_code
    except MissingSchema:
        return get_status_code("https://" + url)


def count_stats(acc, is_ok):
    """
    Increment pair counter based on value of boolean.
    """
    n_ok, n_fail = acc
    return (n_ok + 1, n_fail) if is_ok else (n_ok, n_fail + 1)


def main():
    description = 'Displays site status for polybar.'
    parser = ap.ArgumentParser(description)
    parser.add_argument(
        '-s',
        '--symbolic',
        help='Displays the results as symbols',
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
        nargs='+',
        type=str,
        action='extend')

    args = parser.parse_args()
    val_dict = make_value_dict(args.symbolic)
    res = ""

    if args.urls is not None:
        stats = map(lambda url: (url, get_status_code(url) == codes.ok),
                    args.urls)
        if args.compact:
            failed = list(filter(lambda url_pr: not url_pr[1], stats))
            count = reduce(count_stats, map(lambda url_pr: url_pr[1], stats))
            count_str = f"{val_dict[True]}: {count[0]}"
            failed_str = f" {val_dict[False]}: {failed.join(' ')}"
            res = count_str + failed_str
        else:
            res = list(
                map(lambda url_pr: f"{url_pr[0]}: {val_dict(url_pr[1])}"))

        res = list(stats)
    else:
        res = "Please pass in valid urls you would like to monitor"

    print(res)
    return res


if __name__ == '__main__':
    main()
