def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return (b)


def ft_find_char(char, a):
    c = ft_len(a)
    n = 0
    x = 0
    b = char
    while c > x:
        if a[x] == b:
            n = n + 1
        x = x + 1
    if n == 1:
        x = 0
        while c > x:
            if a[x] == b:
                return(x)
            x = x + 1
    elif n >= 2:
        x = 0
        max = n
        n = 0
        while c > x:
            if a[x] == b:
                n = n + 1
                if n == 1:
                    o = x
                if n == max:
                    p = x
            x = x + 1
        return o,p
    else:
        return False

