def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return (b)


def ft_find_second_char(char, a):
    d = ft_len(a)
    k = 0
    i = 0
    b = char
    while d > i:
        if a[i] == b:
            k = k + 1
        i = i + 1
    if k == 1:
        return -1
    if k >= 2:
        i = 0
        x = 0
        while d > i:
            if a[i] == b:
                x = x + 1
                if x == 1:
                    z = i
                if x == 2:
                    y = i

            i = i + 1
        return z, y
    else:
        return -2
