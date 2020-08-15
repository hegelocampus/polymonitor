# Polymonitor

Polymonitor can be used as a stand alone CLI tool to quickly check the status of a URL or as a plugin for [polybar](https://github.com/polybar/polybar).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install polymonitor.

```bash
$ pip install polymonitor
```

Alternatively you can clone the git repository and use [Poetry](https://python-poetry.org/docs/) to install it.
```bash
$ git clone https://github.com/hegelocampus/polymonitor
$ cd polymonitor
$ poetry install
```

## Usage
```bash
polymonitor --help 
usage: Displays site status for polybar. [-h] [-s] [-c] [-u URLS [URLS ...]]

optional arguments:
  -h, --help            show this help message and exit
  -s, --symbolic        Displays the results as symbols
  -c, --compact         Reduces the results into a more compact package
  -u URLS [URLS ...], --urls URLS [URLS ...]
                        Pass in URLs to monitor
```

A basic use case would be quickly printing the status of web-apps you'd like to check on:
```bash
$ polymonitor -cu duckduckgo.com google.com google.com/404
Up: 2 Down: google.com/404
```
Note that you do not need to preface the URLs with a protocol (e.g., `https://`). If you do not provide a full URL `https://` will be prefixed to your URL before it is pinged.
  
You can leave off the `-c` flag for more verbose output:
```bash
$ polymonitor -cu duckduckgo.com google.com google.com/404
google.com: Up google.com/404: Down duckduckgo.com: Up
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
