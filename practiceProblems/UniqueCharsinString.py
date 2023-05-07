def unique(s):
    uchars = set()
    for c in s:
        if c in uchars:
            return False
        uchars.add(c)
    return True