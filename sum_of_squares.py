def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def is_square(n):
    if n < 0:
        return False

    if n < 2:
        return (True, n)

    lo = 1
    hi = n 

    while hi - lo > 1:
        test = (hi + lo) >> 1

        test_sq = test * test
        if test_sq < n:
            lo = test
        elif test_sq > n:
            hi = test
        else:
            return (True, test)

    return False

def canonize(list1):
    list1_set = set()

    for val in list1:
        collision = False
        for val2 in list1_set:
            g = gcd(val, val2)

            if is_square(val // g) and is_square(val2 // g):
                collision = True
                break

        if collision:
            list1_set.remove(val2)
            sq1 = is_square(val // g)[1]
            sq2 = is_square(val2 // g)[1]
            sq_sum = sq1 + sq2
            list1_set.add(sq_sum * sq_sum * g)
        else:
            list1_set.add(val)
            
    return list1_set

def equality(list1, list2):
    list1_set = canonize(list1)
    list2_set = canonize(list2)

    return list1_set == list2_set
    
            
