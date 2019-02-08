#include <stdio.h>

int main() 
{
    long long a = -5627509462769880281LL;
    char str[128];

    sprintf(str, "%llx", a);
    printf("%s", str);

    return 0;
}
