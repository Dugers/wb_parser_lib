from wb_parser.config import WbV13URLOffsets, WB_V13_MAX_QUERY_LENGTH

def wb_id_validator(id: int):
    if not isinstance(id, int):
        raise ValueError(f"id must be an int. You got {type(id)}")
    if (id < 0):
        raise ValueError(f"id must be a positive number. You got {id}")
    
    id_min_len = max(WbV13URLOffsets.PRODUCT_PART_FROM_ID_RIGHT_OFFSET, WbV13URLOffsets.PRODUCT_VOL_FROM_ID_RIGHT_OFFSET)
    id_len = len(str(id))
    
    if (id_len < id_min_len):
        raise ValueError(f"id must have len more than {id_min_len}. You got {id}")
    
def wb_query_validator(query: str):
    if not isinstance(query, str):
        raise ValueError(f"query must be a str. You got {type(query)}")
    if (not query):
        raise ValueError("query can't be empty")
    if (len(query) > WB_V13_MAX_QUERY_LENGTH):
        raise ValueError(f"query is too long, max length is {WB_V13_MAX_QUERY_LENGTH}. Your query has {len(query)} length")