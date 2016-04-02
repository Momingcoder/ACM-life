#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>

const int True = 1;
const int False = 0;

int getRandNumber(int left, int right)
{
    srand((unsigned)time(NULL));
    int n = rand() % right;
    while(n < left)
    {
        n = rand() % right;
    }
    return n;
}

int getPow(int n, int e)
{
	int tmp = n;
    while(e-- > 1)
    {
        n *= tmp;
    }
    return n;
}

int isPrime(int n)
// is n a prime, return True or False
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

    int u = n - 1; // u is the exponent
    while(u % 2 == 0)
    {
        u /= 2;
    }

    int i, S = 5; // execute S times
    for(i = 0; i < S; i++)
    {
        int a = getRandNumber(2, n);
        int x = getPow(a, u) % n;
        int y, tmp = u;
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
    int num, i, x;
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
