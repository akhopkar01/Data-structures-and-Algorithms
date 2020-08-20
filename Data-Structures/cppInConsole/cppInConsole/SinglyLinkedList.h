#pragma once
struct node
{
	int data;
	struct node* next{ nullptr };
};
class SinglyLinkedList
{
private:
	node* head{nullptr};
	node* tail{nullptr};
public:
	void append(int);
	void display();
	int access(int);
	void insert_after(int, int);


};

