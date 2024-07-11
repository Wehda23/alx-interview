#!/usr/bin/python3
"""Module contains function to unlockboxs"""


def canUnlockAll(boxes) -> bool:
    """Function to unlock all boxes in a list of boxes"""
    n = len(boxes)
    unlocked = set([0])  # Start with the first box unlocked
    queue = [0]  # Start with the first box in the queue

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                queue.append(key)

    return len(unlocked) == n
