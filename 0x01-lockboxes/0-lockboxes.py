#!/usr/bin/python3
"""You have n number of locked boxes in front of you.
   Each box is numbered sequentially from 0 to n - 1 and 
   each box may contain keys to the other boxes"""

def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    keys = {}
    for box in boxes:
        for key in box:
            if key not in keys:
                keys[key]  = 1
            else:
                keys[key] += 1
    
    for box_label in range(1, len(boxes)):
        if box_label not in keys:
            return False
    return True