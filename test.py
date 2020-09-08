def flb1(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return flb1(n-1) + flb1(n-2)


def flb2(n):
    
    n0, n1 = 0, 1
    for cnt in range(n - 1):
        n0, n1 = n1, n0 + n1
    
    return n1


if __name__ == '__main__':
    print("call flb1")
    for x in range(10):
        print(f'{flb1(x)},', end='')
    print()
    print("call flb2")
    for x in range(10):
        print(f'{flb2(x)},', end='')
    print()