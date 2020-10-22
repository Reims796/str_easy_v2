def ft_len(x):
    c = 0
    for i in x:
        c += 1
    return (c)


def ft_analysis(x):
    print(x[2])
    print(x[ft_len(x) - 2])
    print(x[0], x[1], x[2], x[3], x[4], sep="")
    z = 0
    while z != ft_len(x) - 2:
        print(x[z], end="")
        z += 1
    z = 0
    print(end="\n")
    while z != ft_len(x):
        if z % 2 == 0:
            print(x[z], end="")
        z += 1
    print(end="\n")
    z = 0
    while z != ft_len(x):
        if z % 2 != 0:
            print(x[z], end="")
        z += 1
    print(end="\n")
    z = 0
    while z != ft_len(x):
        print(x[ft_len(x) - z - 1], end="")
        z += 1
    print(end='\n')
    z = 0
    while z != ft_len(x):
        if z % 2 == 0:
            print(x[ft_len(x) - z - 1], end="")
        z += 1
    print(end='\n')
    print(ft_len(x))
