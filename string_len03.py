def main(a,b):
    """
    String type variables a and b are given. Return True if the length is equal. If not equal, return False.
    Args:
        a: string
        b: string
    Returns:
        True or False
    """
    x = len(a)
    y = len(b)

    if x==y:
        print(True)
        return True
    
    else:
        print(False)

    
        return False
   