def join(*args, sep='-'):
    if not args:
        return None

    lst = args[0]
    for a in args[1:]:
        lst.append(sep)
        lst += a

    return lst


print(join())
