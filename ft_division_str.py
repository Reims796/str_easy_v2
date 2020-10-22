def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return (b)


def ft_division_str(a):
    c = ft_len(a)
    x = ''
    z = 0
    n = c
    if c % 2 == 0:
        c = c // 2
        x = a[c:n] + a[z:c]
        return x
    else:
        c = c // 2 + 1
        x = a[c:n] + a[z:c]
        return x



