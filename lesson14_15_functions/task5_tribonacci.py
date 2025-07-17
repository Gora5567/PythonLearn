def tribonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    elif n == 3:
        return [0, 1, 1]

    trib = [0, 1, 1]
    for i in range(3, n):
        trib.append(trib[i-3] + trib[i-2] + trib[i-1])
    return trib