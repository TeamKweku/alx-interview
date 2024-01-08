#!/usr/bin/python3
""" this module contains source code on lockboxes implementation """


def canUnlockAll(boxes):
    """
    Function that takes a list of list and returns
    whether true or false if all boxes(list) can open
    all other boxes in the (list of list)
    """
    if not isinstance(boxes, list):
        return False
    if any(not isinstance(box, list) for box in boxes):
        return False
    if not boxes:
        return False

    opened_boxes = {0}

    keys_to_process = [0]

    while keys_to_process:
        current_box = keys_to_process.pop()

        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                keys_to_process.append(key)
                opened_boxes.add(key)

    return len(opened_boxes) == len(boxes)
