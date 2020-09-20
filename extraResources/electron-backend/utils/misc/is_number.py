def is_number(char):
    try:
        if int(char) >= 0:
            return True
        else:
            return False
    except:
        return False
