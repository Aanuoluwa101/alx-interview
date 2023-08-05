#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[2], [1]]
print(canUnlockAll(boxes))