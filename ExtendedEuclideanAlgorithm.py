
# Application of Extended Euclidean Algorithm to find Multiplicative Inverse Modulo

# find an 'x' such that:
# a * x = 1 (MOD n) => x = inverse(a) (MOD n)
def ex_euclidean_mod_inverse(a, n):
    mod = n  # saving for later use
    r = n % a
    q = n // a
    # n = a * q + r => r = n - a * q
    # so, we store this equation in a list as:
    # li[0] = [n, 1]
    # li[1] = [a, q]
    li = [[n, 1], [a, q]]       # r = (n * 1) - (a * q)
    stack = [li]                # initialize the stack
    while r > 1:
        n = a
        a = r
        r = n % a
        q = n // a
        li = [[n, 1], [a, q]]   # r = (n * 1) - (a * q)
        stack.append(li)        # push this equation on the stack

    if r != 1:
        return 0  # a and n were not co-prime so inverse(a) MOD n does not exist

    eqn = stack.pop()  # our final equation to give remainder as 1

    while stack:  # while stack is not empty
        li = stack.pop()
        # find this remainder
        r = li[0][0] * li[0][1] - li[1][0] * li[1][1]
        # now put this remainder's equivalent into the eqn
        k = eqn[0][1]
        q = eqn[1][1]
        if eqn[0][0] == r:  # either replace 'n'
            li[0][1] *= k
            li[1][1] *= k
            eqn[1][1] += li[1][1]
            eqn[0][0] = li[0][0]
            eqn[0][1] = li[0][1]
        else:               # or replace 'a'
            li[0][1] *= q
            li[1][1] *= q
            eqn[0][1] += li[1][1]
            eqn[1][0] = li[0][0]
            eqn[1][1] = li[0][1]

    # ignoring the factor whose modulo n will be 0
    if eqn[1][0] == mod:
        # here, we have a positive inverse, so return
        return eqn[0][1]
    # we have a negative value
    # we need to return in residue module n i.e. Z(n)
    return mod - eqn[1][1]


if __name__ == '__main__':
    print('x = inverse(a) MOD n')
    a = int(input('Enter a: '))
    n = int(input('Enter n: '))
    x = ex_euclidean_mod_inverse(a, n)
    if x == 0:
        print(a, "and", n, "are not co-prime, so inverse("+str(a)+") modulo", n, "does not exist!")
    else:
        print("x =", x)
