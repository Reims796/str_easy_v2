def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return (b)


def ft_find_char(char, a):
    c = ft_len(a)
    i = 0
    k = 0
    b = char
    while c > i:
        if a[i] == b:
            k = k + 1
        i = i + 1
    if k == 1:
        i = 0
        while c > i:
            if a[i] == b:
                return (i)
            i = i + 1
    elif k >= 2:
        i = 0
        max = k
        k = 0
        while d > i:
            if str[i] == b:
                k = k + 1
                if k == 1:
                    x = i
                if k == max:
                    y = i
            i = i + 1
        return x, y
    else:
        return False
