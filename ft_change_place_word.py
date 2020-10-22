def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return (b)


def ft_change_place_word(a):
    c = ft_len(a)
    n = ''
    v = 0
    x = 0
    z = c
    while c > v:
        if a[v] == ' ':
            x = v + 1
        v = v + 1
    c = z
    v = 0
    n = a[x:c] + ' ' + a[v:x]
    return n
