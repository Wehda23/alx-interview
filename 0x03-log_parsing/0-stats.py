#!/usr/bin/python3
"""
File that parses logs status
"""
import sys
import signal


total_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
line_count = 0


def print_stats():
    """
    Function to print status
    """
    global total_size, status_codes_count
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """
    SIGNAL HANDLER
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 9:
            continue

        ip, dash, date, request, status_code, file_size = (
            parts[0],
            parts[1],
            parts[3],
            parts[5],
            parts[8],
            parts[9],
        )
        if (
            dash != "-"
            or not date.startswith("[")
            or not request.startswith('"GET')
            or not status_code.isdigit()
            or not file_size.isdigit()
        ):
            continue

        total_size += int(file_size)
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

    except Exception:
        continue


# Print final stats if no interruption
print_stats()
