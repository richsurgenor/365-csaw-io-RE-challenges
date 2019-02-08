#include <stdio.h>

int main()
{
    char x[8];
    *(long long *) x =  -5627509462769880281LL;
    
    for (int i = 0; i < 37; i++)
    {
        printf("0x%x\n,", (unsigned char) x[i]);
    }
    
    return 0;
}
