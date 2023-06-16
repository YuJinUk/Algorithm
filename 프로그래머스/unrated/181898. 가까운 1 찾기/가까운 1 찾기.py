def solution(arr, idx):
    for iidx, i in enumerate(arr[idx:]):
        if i: return iidx + idx
    else: return -1