def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return (b)


def ft_division_str(a):
    c = ft_len(a)
    x = ''
    i = 0
    z = c
    if c % 2 == 0:
        c = c // 2
        x = a[c:z] + a[i:c]
        return x
    else:
        c = c // 2 + 1
        x = a[c:z] + a[i:c]
        return x

