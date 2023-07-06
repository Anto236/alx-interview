#!/usr/bin/python3
"""Solution to Lockboxes problem"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    for i in range(1, len(boxes) - 1):
        unlocked = False
        for box in boxes:
            if i in box and i != boxes.index(box):
                unlocked = True
                break
        if not unlocked:
            return False

    return True
