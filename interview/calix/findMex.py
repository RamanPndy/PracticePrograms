def find_mex(array):
    unique_nums = set(array)
    mex = 0

    while mex in unique_nums:
        mex += 1

    return mex
