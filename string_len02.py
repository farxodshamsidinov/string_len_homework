def main(a):
    """
    A string type variable is given. Return True if its length is even. Return False if its length is odd.
    Args:
        a: string
    Returns:
        True or False
    """
    y = len(a)
    if y%2==0:
        print(True)
        return True



    else:
        print(False) 



          
        return False
print(main("hello World"))