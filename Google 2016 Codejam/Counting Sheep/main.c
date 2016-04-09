#include <stdio.h>
#include <stdlib.h>

int is_all_count(int digits[])
{
    int i = 0, flag = 1;
    for(i = 0; i < 10; i++)
    {
        if(digits[i] == 0)
        {
            return 0;
        }
    }
    return flag;
}

int count_sheep(long n)
{
    int i = 0, index, digits[10] = {0};
    long tmp;
    if(n == 0)
    {
        return -1;
    }
    while(1)
    {
        //printf("%d\n", n);
        i++;
        if(is_all_count(digits))
        {
            break;
        }
        if(i > 1000)
        {
            return -1;
        }
        tmp = n * i;
        while(tmp)
        {
            index = tmp % 10;
            digits[index] = 1;
            tmp /= 10;
        }
    }
    return n * (i - 1);
}

int main()
{
    int T;
    int i, result;
    long input;
    FILE *fr = NULL, *fw = NULL;
    if((fr = fopen("./A-large.in", "r")) == NULL)
    {
        exit(1);
    }
    if((fw = fopen("./A-small-result.in", "w")) == NULL)
    {
        exit(1);
    }
    fscanf(fr, "%d\n", &T);
    for(i = 0; i < T && fscanf(fr, "%ld\n", &input) != EOF; i++)
    {
        result = count_sheep(input);
        fprintf(fw, "Case #%d:", i + 1);
        if(result > 0)
        {
            fprintf(fw, "%c%d\n", (char)(32), result);
        }
        else
        {
            fprintf(fw, " INSOMNIA\n");
        }
    }
    /*
    scanf("%d", &T);
    for(i = 0; i < T; i++)
    {
        scanf("%d", &input);
        result = count_sheep(input);
        printf("Case #%d: ", i + 1);
        if(result > 0)
        {
            printf("%d\n", result);
        }
        else
        {
            printf("INSOMNIA\n");
        }
    }
    */
    return 0;
}
