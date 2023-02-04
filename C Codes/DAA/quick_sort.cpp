#include <iostream>
using namespace std;
void quick_sort(int a[]){
    int count = 0;
    int n = sizeof(&a);
    int pivot = a[0];
    int i = 1;
    int j = n-1;
    while(i<=j){
        while(a[i]<pivot){
            i++;
            count = 1;
        }
        while(a[j]>pivot){
            j--;
            count = 2;
        }
        if(i<=j){
            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
            continue;
        }
    }
    int temp1 = a[j];
    a[j] = pivot;
    a[0] = temp1;
    if(count ==0){
        return;
    }
    quick_sort(a);
}
int main(){
    cout << "Enter number of terms for array :";
    int n;
    cin >> n;
    int m[n];
    cout<<"Enter elements for the array :\n";
    
    for(int j=0;j<n;j++){
        cin>>m[j];
    }
    quick_sort(m);
    for(int j=0;j<n;j++){
        cout<<m[j];
    }
}