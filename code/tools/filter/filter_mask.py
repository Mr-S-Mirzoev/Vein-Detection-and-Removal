from numpy import int64
normalized = 0x000001
equalized  = 0x000010

def is_equalized(value: int64):
    assert value >= 0
    return bool(value & equalized)

def is_normalized(value: int64):
    assert value >= 0
    return bool(value & normalized)

def get_bit_mask(values: dict):
    bitmask = 0

    if '-MEDIAN-' in values:
        bitmask |= normalized

    if '-EQUALIZE-' in values:
        bitmask |= equalized

    return bitmask
