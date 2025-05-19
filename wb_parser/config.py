from enum import IntEnum, StrEnum

class WbV13URLOffsets(IntEnum):
    PRODUCT_VOL_FROM_ID_RIGHT_OFFSET = 5
    PRODUCT_PART_FROM_ID_RIGHT_OFFSET = 3

class WbV13FindParams(StrEnum):
    RESULTSET = "catalog"
    DEST = "-5854091"

WB_V13_MAX_QUERY_LENGTH = 256