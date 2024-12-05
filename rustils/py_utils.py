def py_str_to_bool(s: str) -> bool:
    """Python implementation of string to boolean conversion"""
    s = s.lower()
    if s in ('true', '1', 'yes', 'y', 'on'):
        return True
    if s in ('false', '0', 'no', 'n', 'off'):
        return False
    raise ValueError(f"Cannot convert '{s}' to bool")
