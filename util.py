def bytes_to_int(self, bytes, order='little'):
    try:
        result = int.from_bytes(bytes, order)
    except Exception as e:
        raise e
    return result