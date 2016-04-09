#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_all_happy(char pancakes[], int n)
{
    int i = 0;
    for(i = 0; i < n; i++)
    {
        if(pancakes[i] == '-')
        {
            return 0;
        }
    }
    return 1;
}

int get_first_target(char pancakes[], int n, int start, char target)
{
    int i = 0;
    for(i = start; i < n; i++)
    {
        if(pancakes[i] == target)
        {
            return i;
        }
    }
    return n;
}

int get_min_choice(char pancakes[], int n)
{
    int time = 0, start, end, j = 0;
    while(!is_all_happy(pancakes, n))
    {
        start = get_first_target(pancakes, n, 0, '-');
        if(start == 0)
        {
            end = get_first_target(pancakes, n, start, '+');
            for(j = 0; j < end; j++)
            {
                pancakes[j] = '+';
            }
        }
        else
        {
            for(j = 0; j < start; j++)
            {
                pancakes[j] = '-';
            }
        }

        time++;
    }
    return time;
}

int main()
{
    int T, i = 0, result, length;
    //char *input = NULL, *p = NULL;
    char input[200];
    //int pancakes[10] = {0};
    FILE *fr = NULL, *fw = NULL;
    if((fr = fopen("./B-large.in", "r")) == NULL)
    {
        exit(1);
    }
    if((fw = fopen("./result.in", "w")) == NULL)
    {
        exit(1);
    }
    fscanf(fr, "%d\n", &T);
    for(i = 0; i < T && fgets(input, 2048, fr) != NULL; i++)
    {
        length = strlen(input);
        //printf("%s\n", input);
        /*
        for(j = 0; j < 10; j++)
        {
            pancakes[j] = 0;
        }

        for(j = 0; j < length; j++)
        {
            if(input[j] == '+')
            {
                pancakes[j] = 1;
            }
            else if(input[j] == '-')
            {
                pancakes[j] = -1;
            }
        }
        */
        /*
        for(j = 0; j < 10; j++)
        {
            printf("%d ", pancakes[j]);
        }
        */
        result = get_min_choice(input, length);
        fprintf(fw, "Case #%d: %d\n", i + 1, result);
    }
    fclose(fr);
    fclose(fw);
    return 0;
}
