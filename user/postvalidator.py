def validate(data,*args):
    for i in args:
        if i not in data.keys():
            return False
    return True