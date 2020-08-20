// cppInConsole.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <vector>
#include "SinglyLinkedList.h"
#include "Stack.h"
#include "Queue.h"

SinglyLinkedList* create_linked_list(int*, int, bool);
Stack* create_stack(int*, int);
Queue* generate_queue(int*, int);

SinglyLinkedList* create_linked_list(int* arr, int n, bool disp = false) {
    SinglyLinkedList* head = new SinglyLinkedList;
    for (int index = 0; index < n; index++) {
        head->append(arr[index]);
    }
    if (disp == true) {
        head->display();
    }

    return head;
}

Stack* create_stack(int* arr, int n) {
    Stack* stack = new Stack;
    for (int i = 0; i < n; i++) {
        stack->push(arr[i]);
    }
    return stack;
}

Queue* generate_queue(int* arr, int n) {
    Queue* queue = new Queue;
    for (int i = 0; i < n; i++) {
        queue->push(arr[i]);
    }
    return queue;
}

int main()
{   

    std::vector<int> v;

    int arr[100]{};
    int n;

    std::cout << "Enter the number of elements in your Data Structure ";
    std::cin >> n;

    std::cout << " Enter the data " << std::endl;
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

   SinglyLinkedList* list_from_array = create_linked_list(arr, n);
   list_from_array->insert_after(2, 10);
   //list_from_array->display();

   Stack* stack = create_stack(arr, n);
   //stack->display_stack();
   int element = stack->pop();
   std::cout <<"\n Pop Stack: "<< element << std::endl;
   //stack->display_stack();

   Queue* queue = generate_queue(arr, n);
   queue->display_queue();
   std::cout << "Pop queue " << queue->pop() << std::endl;

    delete list_from_array;
    list_from_array = nullptr;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
