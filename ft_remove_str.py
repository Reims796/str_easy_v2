def ft_len(b):
    a = 0
    for i in b:
        a += 1
    return a


def ft_remove_str(d, x):
    c = 0
    b = ''
    for i in d:
        if i in x:
            c += 1
        else:
            b += i
    if ft_len(d) == c:
        return False
    else:
        return b
