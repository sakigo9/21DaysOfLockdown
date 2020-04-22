#include<stdio.h>
#include<stdlib.h>

    struct Node* head;  //pointer to head Node + Global 
    
	void Insert(int s);
	void Print();
	 
	struct Node{
	int data;
	struct Node* next;
	};
	
	
	void Insert(int x){
		
		struct Node* temp=(struct Node*)malloc(sizeof(struct Node));
		temp->data=x;   //temp is pointer variable so we are derefrencing the pointer variable to assign that with some value
//	1	(*temp).next=NULL;  // OR temp->next=NULL;
//	2	if (head!=NULL) temp->next=head;
      // below works same as that of 1 and 2
        temp->next=head;

		head=temp;
		
	}
	void Print(){
		struct Node* temp=head;
		while(temp!=NULL){
			
			printf("%d",temp->data);
			temp=temp->next;
		}
		printf("\n");
	}
	
	
	
	
	
	
int main()
	{
		
		head=NULL;  // Starting Node pointing to Null as default defination
		int n,i,x;
		printf("Enter the no of Numbers\n");
		scanf("%d",&n);
		for(i=0;i<n;i++){
			printf("enter the number\n");
			scanf("%d",&x);
			Insert(x);
			Print();
		}
	}
	
	
	
