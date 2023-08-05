#!/usr/bin/python3
"""You have n number of locked boxes in front of you. 
   Each box is numbered sequentially from 0 to n - 1 
   and each box may contain keys to the other boxes"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    unlocked_boxes = set([0])  
    all_keys = [0]

    if not boxes:
        return False
    
    while all_keys:
        current_box = all_keys.pop(0)

        if current_box < len(boxes):
            box_keys = boxes[current_box]
            
            for key in box_keys:
                if key not in unlocked_boxes:
                    unlocked_boxes.add(key)
                    all_keys.append(key)

    for box in range(len(boxes)):
        if box not in unlocked_boxes:
            return False
    return True
