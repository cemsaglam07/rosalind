from contextlib import closing
from urllib.request import urlopen


def fafsa(*filenames):
    data = {}
    for filename in filenames:
        tmp = ""
        if filename[-4::] == ".txt":
            with open(filename, "r") as f:
                raw = f.read().splitlines()
            for item in raw:
                if len(item) > 0 and item[0] == ">":
                    tmp = item[1:]
                    data[tmp] = ""
                else:
                    data[tmp] += item
        elif filename[:7] == "http://":
            with closing(urlopen(filename)) as raw:
                for item in raw:
                    item = str(item)[2:-3:]
                    if len(item) > 0 and item[0] == ">":
                        tmp = item[1:]
                        data[tmp] = ""
                    else:
                        data[tmp] += item
    return data
