#pragma once
#include <vector>

class Stack
{
private:
	std::vector<int>* vec = new std::vector<int>;
public:
	void push(int);
	int pop();
	bool is_empty();
	void display_stack();
};

