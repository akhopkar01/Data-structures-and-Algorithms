#include "Stack.h"
#include <iostream>

void Stack::push(int data)
{
	vec->push_back(data);
}

int Stack::pop()
{
	int val = vec->back();
	vec->pop_back();
	return val;
}

bool Stack::is_empty()
{
	if (vec->size() == 0) return true;
	else return false;
}

void Stack::display_stack()
{
	std::cout << "---Stack Bottom---\n";
	for (const int& element : *vec) {
		std::cout << "---"<<element << "---\n";
	}
	std::cout << "---Stack top---\n" << std::endl;
}
