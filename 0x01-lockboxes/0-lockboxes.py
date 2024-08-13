#!/usr/bin/python3
"""Script to unlock list"""


def canUnlockAll(boxes):
    """The function take a list of lists and the content"""

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
