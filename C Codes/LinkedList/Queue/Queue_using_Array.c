#include <stdio.h>
#include <stdlib.h>
struct queue{
    int size;
    int f;
    int r;
    int *arr;
};
int isFull(struct queue *q){
    if(q->r==q->size-1){
        return 1;
    }
    return 0;
}
int isEmpty(struct queue *q){
    if(q->r==q->f){
        return 1;
    }
    return 0;
}
void enqueue(struct queue *q, int val){
    if(isFull(q)){
        printf("This Queue is full\n");
    }
    else{
        q->r++;
        q->arr[q->r] = val;
        printf("Enqued element: %d\n", val);
    }
}
int dequeue(struct queue *q){
    int a = -1;
    if(isEmpty(q)){
        printf("This Queue is empty\n");
    }
    else{
        q->f++;
        printf("Dequed Element : %d\n",q->arr[q->f]);
        a = q->arr[q->f]; 
    }
    return a;
}
int main(){
    struct queue *q;
    q->size = 3;
    q->f = -1;
    q->r = -1;
    q->arr = (int *)malloc(q->size*sizeof(int));
    enqueue(q,5);
    enqueue(q,10);
    enqueue(q,15);
    if(isFull(q)){
        printf("The Queue is Full.\n");
    }
    dequeue(q);
    dequeue(q);
    dequeue(q);
    if(isEmpty(q)){
        printf("The Queue is empty.\n");
    }
    return 0;
}