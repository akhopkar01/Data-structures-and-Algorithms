// cppInConsole.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <vector>
#include "SinglyLinkedList.h"
#include "Stack.h"
#include "Queue.h"
#include <string>


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
    int choice;
    int data{ 0 }, idx{0};

    std::cout << "Enter the number of elements in your Data Structure: ";
    std::cin >> n;
    
    std::cout << "Enter the data: ";
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
    
    std::cout << "Choose your data structure - (1) Linked List (2) Stack (3) Queue: ";
    std::cin >> choice;

// Improve this using Polymorphism later.
    SinglyLinkedList* list_from_array = create_linked_list(arr, n);
    Stack* stack = create_stack(arr, n);
    Queue* queue = generate_queue(arr, n);

    switch (choice) {
    case 1:
        int lchoice;
        
        list_from_array->display();
        std::cout << "Choose operation - (1) Insert After node (2) Access (3) Append: ";
        std::cin >> lchoice;
        if (lchoice == 1) {
            std::cout << "Enter index and data to insert after: ";
            std::cin >> idx >> data;
            list_from_array->insert_after(idx, data);
            list_from_array->display();
        }
        else if (lchoice == 2) {
            std::cout << "Enter index to access : ";
            std::cin >> idx;
            std::cout << list_from_array->access(idx) << std::endl;
        }
        else if (lchoice == 3) {
            std::cout << "Enter data to append: ";
            std::cin >> data;
            list_from_array->append(data);
            list_from_array->display();
        }
        else std::cout << "[ERROR] Invalid Entry! " << std::endl;

        break;

    case 2:
        int schoice;
        
        stack->display_stack();
        std::cout << "Choose operation - (1) Push (2) Pop ";
        std::cin >> schoice;
        if (schoice == 1) {
            std::cout << "Enter data to push: ";
            std::cin >> data;
            stack->push(data);
            stack->display_stack();
        }
        else if (schoice == 2) {
            std::cout << "Popped element: " << stack->pop()<< std::endl;
            stack->display_stack();
        }
        else std::cout << "[ERROR] Invalid Entry! " << std::endl;
        break;

    case 3:
        int qchoice;
        
        queue->display_queue();
        std::cout << "Choose operation - (1) Push (2) Pop ";
        std::cin >> qchoice;
        if (qchoice == 1) {
            std::cout << "Enter data to push: ";
            std::cin >> data;
            queue->push(data);
            queue->display_queue();
        }
        else if (qchoice == 2) {
            std::cout << "Popped element: " << queue->pop() << std::endl;
            queue->display_queue();
        }
        else std::cout << "[ERROR] Invalid Entry! " << std::endl;

        break;

    default:
        std::cout << "[INFO] Default Array \n";
        for (int i = 0; i < n; i++) {
            std::cout << arr[i] << " ";
        }



    }
    
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
