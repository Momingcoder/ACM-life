# -*- coding: utf-8 -*-
# @Author: Moming

import random

def getRandNumber(right):
    list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    n = random.randint(0, 11)
    while list[n] >= right:
        n = random.randint(0, 11)

    return list[n]

def getMontgomeryPow(n, e, m):
    tmp = 1
    while e > 0:
        if (e & 1) == 1:
            tmp = (tmp * n) % m

        n = (n * n) % m;
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

# main
num = int(input())
for i in range(num):
    n = int(input())
    if isPrime(n):
        print 'Yes'
    else:
        print 'No'
