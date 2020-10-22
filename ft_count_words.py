def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return (b)


def ft_count_words(a):
    x = 0
    d = ft_len(a)
    i = 0
    if a[0] == ' ':
        while i < d:
            if a[i] == ' ' and a[i - 1] != ' ':
                x = x + 1
            i = i + 1
        return x
    else:
        while i < d:
            if a[i] == ' ' and a[i - 1] != ' ':
                x = x + 1
            i = i + 1
        return x + 1
