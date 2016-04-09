#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>

const int True = 1;
const int False = 0;

int getRandNumber(long limit)
{
    srand((unsigned)time(NULL));
    int n = rand() % 12;
    int list[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    while(list[n] >= limit)
    {
        n = rand() % 12;
    }
    return list[n];
}

long getMontgomeryPow(int n, long e, long m)
{
	long tmp = 1;
    while(e > 0)
    {
        if((e & 1) == 1)
        {
            tmp = (tmp * n) % m;
        }
        n = (n * n) % m;
        e >>= 1;
    }
    return tmp;
}

int isPrime(long n)
// is n a prime? return True or False
{
    // is n <= 2
    if(n <= 2)
    {
        if(n == 2)
        {
            return True;
        }
        return False;
    }

    // is n an even
    if(n % 2 == 0)
    {
        return False;
    }

    long u = n - 1; // u is the exponent
    while(u % 2 == 0)
    {
        u /= 2;
    }

    int i, S = 5; // execute S times
    for(i = 0; i < S; i++)
    {
        int a = getRandNumber(n);
        long x = getMontgomeryPow(a, u, n);
        long y, tmp = u;
        while(tmp < n)
        {
            y = (x * x) % n;
            if(y == 1 && x != 1 && x != n - 1)
            {
                return False;
            }
            x = y;
            tmp *= 2;
        }
        if(x != 1)
        {
            return False;
        }
    }
    return True;
}

int main(void)
{
    int i, num;
	long x;
    scanf("%d", &num);
    for(i = 0; i < num; i++)
    {
        scanf("%d", &x);
		//printf("x = %d is Prime? ", x);
        if(isPrime(x))
        {
            printf("Yes\n");
        }
        else
        {
            printf("No\n");
        }
    }
    return 0;
}
