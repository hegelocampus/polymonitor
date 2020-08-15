#!/usr/bin/env python3

import argparse as ap
from requests import get, codes
from requests.exceptions import InvalidURL
from validators import url as valid_url
from termcolor import colored


def make_value_dict(symbolic):
    map_to_res = {
        True: "\uf062" if symbolic else "Up",
        False: "\uf98d" if symbolic else "Down"
    }

    return map_to_res


def get_status_code(url):
    """
    Gets the current status code of a full url or short url. Short urls will
    be prepended with https.
    """
    if valid_url(url):
        return get(url).status_code
    elif valid_url("https://" + url):
        return get("https://" + url).status_code
    else:
        raise InvalidURL(f"{url} isn't a valid URL!")


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
        action='store_true'
    )
    parser.add_argument(
        '-c',
        '--compact',
        help='Reduces the results into a more compact package',
        action='store_true'
    )
    parser.add_argument(
        '-u',
        '--urls',
        help='Pass in URLs to monitor',
        nargs='+',
        type=str,
        action='extend'
    )

    args = parser.parse_args()
    val_dict = make_value_dict(args.symbolic)
    res = ""

    if args.urls is not None:
        stats = map(lambda url: (url, get_status_code(url) == codes.ok),
                    args.urls)
        if args.compact:
            failed = []
            count = [0, 0]
            for url, is_ok in stats:
                if is_ok:
                    count[0] += 1
                else:
                    count[1] += 1
                    failed.append(url)

            count_str = f"{val_dict[True]}: {count[0]}"
            failed_str = val_dict[False] + ': '
            if failed:
                failed_str = colored(failed_str + ' '.join(failed), 'red')
            else:
                failed_str += '0'
            res = count_str + " " + failed_str
        else:
            res = ' '.join(list(
                map(lambda url_pr: f"{url_pr[0]}: {val_dict[url_pr[1]]}",
                    stats)
            ))

    else:
        res = "Please pass in valid urls you would like to monitor"

    return res


if __name__ == "__main__":
    print(main())
