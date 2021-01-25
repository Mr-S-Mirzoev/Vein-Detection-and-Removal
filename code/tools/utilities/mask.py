from numpy import int64

g_equalized = 0x000001
equalized   = 0x000010
median      = 0x000100
gaussian    = 0x001000
filter1     = 0x010000
filter2     = 0x100000

########################################
# Check by mask if filter is triggered #
########################################
def is_equalized(value: int64):
    assert value >= 0
    return bool(value & equalized)

def is_g_equalized(value: int64):
    assert value >= 0
    return bool(value & g_equalized)

def is_median(value: int64):
    assert value >= 0
    return bool(value & median)

def is_gaussian(value: int64):
    assert value >= 0
    return bool(value & gaussian)

def is_filter1(value: int64):
    assert value >= 0
    return bool(value & filter1)

def is_filter2(value: int64):
    assert value >= 0
    return bool(value & filter2)

#################################################
# Create a bit mask from values of GUI response #
#################################################
def get_bit_mask(values: dict):
    bitmask = 0

    if values['-GRAY-EQUALIZE-']:
        bitmask |= g_equalized

    if values['-EQUALIZE-']:
        bitmask |= equalized

    if values['-MEDIAN-']:
        bitmask |= median

    if values['-GAUSSIAN-']:
        bitmask |= gaussian

    return bitmask
