#!/usr/bin/python
# -*- coding: utf-8 -*-
# python 2.7
# @Author: Moming

import random

def getRandNumber(right):
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    n = random.randint(0, 11)
    while prime_list[n] >= right:
        n = random.randint(0, 11)

    return prime_list[n]


def getMontgomeryPow(n, e, m):
    tmp = 1
    while e > 0:
        if (e & 1) == 1:
            tmp = (tmp * n) % m

        n = (n * n) % m
        e = e >> 1

    return tmp


def isPrime(n):
    if n <= 2:
        if n == 2:
            return True
        return False

    if n % 2 == 0:
        return False

    u = n - 1
    while u % 2 == 0:
        u = u // 2

    S = 5
    for i in range(S):
        a = random.randint(2, n - 1)
        x = getMontgomeryPow(a, u, n)
        tmp = u
        while tmp < n:
            y = (x * x) % n
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
            tmp = tmp * 2

        if x != 1:
            return False

    return True

"""
def getPow(n, e):
    tmp = 1
    while e > 0:
        if (e & 1) == 1:
            tmp = tmp * n

        n = n * n
        e = e >> 1

    return tmp
"""

def getBinary(j, N):
    cmd = bin(j).replace('0b', '')
    length = N - 2 - len(cmd)
    cmd = '1' + '0' * length + cmd + '1'
    return int(cmd)


"""
def getDecimal(n, base):
    if base == 10:
        return n

    result = 0
    e = 1
    while n:
        if 1 == n % 10:
            result += e

        e *= base
        n /= 10

    return result
"""

def gcd(x, y):
    if x < y:
        return gcd(y, x)
    if y == 0:
        return x
    else:
        if x & 1 == 0:
            if y & 1 == 0:
                return (gcd(x >> 1, y >> 1) << 1)
            else:
                return gcd(x >> 1, y)
        else:
            if y & 1 == 0:
                return gcd(x, y >> 1)
            else:
                return gcd(y, x - y)


def factor_g1(x, n):
    return (x * x + 1) % n

def factor_g2(x, n):
    return (x * x - 1) % n

def getFactor(n):
    x = 2
    y = 2
    d = 1
    g = factor_g1
    while d == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        d = gcd(abs(x - y), n)
        if d == n and g == factor_g1:
            g = factor_g2
        elif d == n and g == factor_g2:
            return -1

    return d

def his_gcd(x, y):
    while y != 0:
        remainder = x % y
        x = y
        y = remainder

    return x

def his_factor(n):
    x_fixed, cycle_size, x, factor = 2, 2, 2, 1
    while factor == 1:
        count = 1
        while count <= cycle_size and factor <= 1:
            x = (x * x + 1) % n
            factor = his_gcd(x - x_fixed, n)
            count += 1

        cycle_size *= 2
        x_fixed = x

    if factor == n:
        return -1

    return factor


# main
if __name__ == '__main__':
    fr = open('./C-large.in', 'r')
    fw = open('./result_reverse.in', 'w')
    T = int(fr.readline())

    for i in range(T):
        cmd = fr.readline().split(' ')
        (N, J) = (int(x) for x in cmd)
        #print N, J
        fw.write('Case #%d:\n' % (i + 1))

        num = 0
        index = int('1' * (N - 2), 2)
        limit = 0

        while index > limit:
        #for j in range(0, int('1' * (N - 2), 2) + 1):
            if num >= J:
                break

            j = getBinary(index, N)
            flag = True
            tmp = []
            for base in range(2, 11):
                tmp.append(int(str(j), base))
                if isPrime(tmp[base - 2]):
                    flag = False
                    break

            if flag:
                num = num + 1
                fw.write('%d' % j)
                for base in range(2, 11):
                    # factorization

                    if tmp[base - 2] % 2 == 0:
                        fw.write(' 2')
                        continue

                    remain = his_factor(tmp[base - 2])
                    if remain == -1:
                        remain = 1
                        while remain < tmp[base - 2]:
                            remain += 2
                            if isPrime(remain):
                                if tmp[base - 2] % remain == 0:
                                    fw.write(' %d' % remain)
                                    break
                    else:
                        fw.write(' %d' % remain)

                fw.write('\n')

            index = index - 1

    fr.close()
    fw.close()

