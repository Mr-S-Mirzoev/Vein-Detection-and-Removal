from numpy import int64
g_equalized = 0x000001
equalized   = 0x000010
median      = 0x000100

def is_equalized(value: int64):
    assert value >= 0
    return bool(value & equalized)

def is_g_equalized(value: int64):
    assert value >= 0
    return bool(value & g_equalized)


def is_median(value: int64):
    assert value >= 0
    return bool(value & median)

def get_bit_mask(values: dict):
    bitmask = 0

    if values['-GRAY-EQUALIZE-']:
        bitmask |= g_equalized

    if values['-EQUALIZE-']:
        bitmask |= equalized

    if values['-MEDIAN-']:
        bitmask |= median

    return bitmask
