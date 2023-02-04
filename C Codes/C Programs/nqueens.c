#include <stdio.h>
#include <stdbool.h>
int arr[100][100];
bool isSafe(int row, int col,int n){
    int i,j;
    for(j = 0;j<col;j++){
        if(arr[row][j]){
            return false;
        }
    }
    for(i = row,j = col; i>=0 && j>=0; i--,j--){
        if(arr[i][j]){
            return false;
        }
    }
    for(i = row,j = col; i<n && j>=0; i++,j--){
        if(arr[i][j]){
            return false;
        }
    }
}
bool solveNQ(int col,int n){
    if (col >= n){
        return 1;
    }
    for(int i = 0;i<n;i++){
        if(isSafe(i,col,n)){
            arr[i][col] = 1;
            if(solveNQ(col+1,n)){
                return 1;
            }
            arr[i][col] = 0;
        }
    }
    return false;
}
void printSolution(int n)
{
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            printf(" %d ", arr[i][j]);
        printf("\n");
    }
}
bool queen(){
    int n;
    printf("Enter a number :");
    scanf("%d",&n);
    int i, j;
    for (i = 0; i<n; i++)
    {
        for (j = 0; j<n; j++)
        arr[i][j] = 0;
    }
    if (solveNQ(0,n) == 0){
        printf("Solution does not exist !!!");
        return 0;
    }
    printSolution(n);
    return true;
}
int main(){
    queen();
    return 0;
}