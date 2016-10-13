import numpy as np

from utils.sort_scans import sort_groups


def split_scans(scans, split, names, pathOut, classes=None):
    assert sum(split) == 1.0, \
        "Sum of splits is not equal to 1.0."
    assert len(split) == len(names), \
        "Number of splits is not equal to number of provided names."

    imageID_split = []
    for _ in split:
        imageID_split.append([])

    maxValue = 999999999
    maxCounts = np.full(len(split), maxValue, dtype=np.int)

    groups, names = sort_groups(scans)
    minGroup = maxValue
    for g in groups:
        if len(g) < minGroup:
            minGroup = len(g)
    maxCounts[0] = minGroup * split[0]

    indices = np.zeros(len(groups), dtype=np.int)
    for i in range(split):
        for g in groups:
            if indices[i] < maxCounts[i]:




    if classes is None:
        classes = names