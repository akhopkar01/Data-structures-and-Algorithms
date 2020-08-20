#include "SinglyLinkedList.h"
#include <iostream>

void SinglyLinkedList::append(int data)
{
    node* current = new node;
    current->data = data;
    current->next = nullptr;
    if (head == nullptr) {
        head = current;
        tail = current;
    }
    else {
        tail->next = current;
        tail = tail->next;
    }
}

void SinglyLinkedList::display()
{
    node* current = new node;
    current = head;
    while (current != nullptr) {
        std::cout << current->data << "->";
        current = current->next;
    }
}

int SinglyLinkedList::access(int index)
{
    node* current = new node;
    current = head;
    int idx = 0;
    int val;

    if (current == nullptr) {
        std::cout << "Cannot Access!" << std::endl;
        return -1;
    }

    while (current != nullptr) {
        if (idx == index) {
            val = current->data;
            //std::cout << &val << std::endl;
        }
        current = current->next;
        idx++;
    }
    return val;
}

void SinglyLinkedList::insert_after(int index, int data)
{
    node* current = new node;
    node* temp = new node;
    
    current = head;
    temp->data = data;
    temp->next = nullptr;
    int idx = 0;
    while (current != nullptr) {
        if (idx == index) {
            temp->next = current->next;
            current->next = temp;
            break;
        }
        current = current->next;
        idx++;
    }

}
