#include<stdio.h>
#include<stdlib.h>

struct Node* head;

void Insert(int x);
void Print();
void Delete(n);

struct Node{
	int data;
	struct Node *next;
};
void Print(){
	struct Node* temp=head;
	while(temp->next!=NULL){
		printf("%d\n",temp->data);
		temp=temp->next;
	}
}

void Delete(int n){
	int i;
	struct Node* temp1=head;
	if (n==1){
		head=temp1->next;
		free(temp1);
		return;
	}
	for(i=0;i<n-2;i++)
	{
		temp1=temp1->next;  //temp1 points to (n-1) Node
	
	struct Node* temp2=temp1->next;   //nth node
	temp1->next=temp2->next;
	free(temp2);
	
}	
}

void Insert(int data){
	struct Node* temp=(struct Node*)malloc(sizeof(struct Node));
		temp->data=data; 
		temp->next=head;

		head=temp;
	
	
}
int main(){
	head=NULL;

	Insert(3);
	Insert(4);
	Insert(6);
	Insert(8);
	Print();
	int n;
	printf("Enter position of the Node\n");
	
	scanf("%d",&n);
	Delete(n);
	Print();
	
}