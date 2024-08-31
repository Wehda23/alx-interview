#!/usr/bin/python3
"""
Log parsing solution
"""

import sys

if __name__ == "__main__":

    file_size, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def stdo_status(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status = data[-2]
                if status in stats:
                    stats[status] += 1
            except BaseException:
                pass
            try:
                file_size += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                stdo_status(stats, file_size)
        stdo_status(stats, file_size)
    except KeyboardInterrupt:
        stdo_status(stats, file_size)
        raise
