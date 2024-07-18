#!/usr/bin/env python3
"""
Log Parsing Script
"""

import sys


def print_stats(stats: dict, total_size: int) -> None:
    """
    Print the accumulated statistics and total file size.
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(stats.items()):
        if count:
            print("{}: {}".format(code, count))


def main():
    """
    Main function to process log lines from standard input.
    """
    total_size, line_count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    statistics = {code: 0 for code in status_codes}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) < 2:
                continue

            # Update status code statistics
            status_code = parts[-2]
            if status_code in statistics:
                statistics[status_code] += 1

            # Update total file size
            try:
                total_size += int(parts[-1])
            except ValueError:
                pass

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats(statistics, total_size)

        # Final statistics printout
        print_stats(statistics, total_size)

    except KeyboardInterrupt:
        print_stats(statistics, total_size)
        raise


if __name__ == "__main__":
    main()
