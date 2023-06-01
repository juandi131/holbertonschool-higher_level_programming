#include "stdio.h"
int main(void)
{
    int i;
    char *str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax";

    for (i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == 'w' && str[i + 1] == 'i')
        {
            printf("%d\n", i);
        }
    }
    return (i);
}