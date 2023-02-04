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
int isBST(struct Node *root){
    static struct Node *prev = NULL;
    if(root!=NULL){
        if(!isBST(root->left)){
            return 0;
        }
        if(prev!=NULL && root->data <= prev->data){
            return 0;
        }
        prev = root;
        return isBST(root->right);
    }
    else{
        return 1;
    }
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
struct Node * search(struct Node *root,int key){
    if(root == NULL){
        return NULL;
    }
    if(root->data == key){
        return root;
    }
    else if(root->data > key){
        return search(root->left,key);
    }
    else{
        return search(root->right,key);
    }
}
struct Node * itersearch(struct Node *root,int key){
    while(root!=NULL){
        if(key == root->data){
            return root;
        }
        else if(key<root->data){
            root = root->left;
        }
        else{
            root = root->right;
        }
    }
    return NULL;
}
void insertion(struct Node *root,int key){
    struct Node *prev = NULL;
    while(root!=NULL){
        prev = root;
        if(key == root->data){
            printf("\nInsertion not possible !!!");
            return;
        }
        else if(key<root->data){
            root = root->left;
        }
        else{
            root = root->right;
        }
    }
    struct Node *ptr = createaNode(key);
    if(key<prev->data){
        prev->left = ptr;
    }
    else{
        prev->right = ptr;
    }
}

int main(){
    struct Node *p = createaNode(5);
    struct Node *p1 = createaNode(3);
    struct Node *p2 = createaNode(6);

    p->left = p1;
    p->right = p2;

    struct Node *p3 = createaNode(1);
    struct Node *p4 = createaNode(4);

    p1->left = p3;
    p1->right = p4;
    printf("The PreOrder of the Tree is:\n");
    preorder(p);
    printf("\nThe PostOrder of the Tree is:\n");
    postorder(p);
    printf("\nThe InOrder of the Tree is:\n");
    inorder(p);
    if(isBST(p)){
        printf("\nThis is a BST.\n");
    }
    else{
        printf("This is not a BST.\n");
    }
    struct Node * n = search(p,6);
    if(n!=NULL){
        printf("FOUND : %d",n->data);
    }
    else{
        printf("ELEMENT NOT PRESENT IN BST.\n");
    }
    n = search(p,10);
    if(n!=NULL){
        printf("FOUND : %d",n->data);
    }
    else{
        printf("\nELEMENT NOT PRESENT IN BST.\n");
    }
    struct Node * m = itersearch(p,6);
    if(m!=NULL){
        printf("FOUND : %d",m->data);
    }
    else{
        printf("ELEMENT NOT PRESENT IN BST.\n");
    }
    printf("\nBy iterative METHOD: \n");
    m = itersearch(p,10);
    if(m!=NULL){
        printf("FOUND : %d",m->data);
    }
    else{
        printf("\nELEMENT NOT PRESENT IN BST.\n");
    }
    insertion(p,10);
    printf("The PreOrder of the Tree is:\n");
    preorder(p);
    insertion(p,2);
    printf("The PreOrder of the Tree is:\n");
    preorder(p);
    insertion(p,6);
    return 0;
}