#include <stdio.h>
#include <math.h>

int main()
{
    int n,x,y;
    printf("Program to print Umami Prime Spiral...\n");
    printf("Enter a number :");
    scanf("%d",&n);
    
    int val = 1;
    int a[n][n];

    int i = n/2;
    int j = n-1-i;

    int count = 1;
    int k;
    int target = n*n + 1;
    while(val != target){

        for(k=0;k < (int)sqrt(val);val++){
            a[i][j] = val;
            switch(count){

                case 0:
                i+=1;
                break;

                case 1:
                j+=1;
                break;

                case 2:
                i-=1;
                break;

                case 3:
                j-=1;
                break;
            }
        }
        count = (count+1)%4;
    }
    for(x=0;x<n;x++){
        for(y=0;y<n;y++){
            printf("%d ",a[x][y]);
        }
        printf("\n");
    }

    return 0;
}
