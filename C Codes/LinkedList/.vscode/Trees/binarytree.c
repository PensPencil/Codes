#include <stdio.h>
#include <malloc.h>
struct Node{
    int data;
    struct Node *left;
    struct Node *right;
};
struct Node* createaNode(int data){
    struct Node *n = (struct Node *)malloc(sizeof(struct Node));
    n->data = data;
    n->left = NULL;
    n->right = NULL;
    return n;
}
void preorder(struct Node * root){
        
    if(root!=NULL){
        printf("%d ",root->data);
        preorder(root->left);
        preorder(root->right);
    }
}
void postorder(struct Node * root){
        
    if(root!=NULL){
        postorder(root->left);
        postorder(root->right);
        printf("%d ",root->data);
    }
}
void inorder(struct Node *root){
    if(root!=NULL){
        inorder(root->left);
        printf("%d ",root->data);
        inorder(root->right);
    }
}
int main(){
    struct Node *p = createaNode(4);
    struct Node *p1 = createaNode(1);
    struct Node *p2 = createaNode(6);

    p->left = p1;
    p->right = p2;

    struct Node *p3 = createaNode(5);
    struct Node *p4 = createaNode(2);

    p1->left = p3;
    p1->right = p4;
    printf("The PreOrder of the Tree is:\n");
    preorder(p);
    printf("\nThe PostOrder of the Tree is:\n");
    postorder(p);
    printf("\nThe InOrder of the Tree is:\n");
    inorder(p);
    return 0;
}