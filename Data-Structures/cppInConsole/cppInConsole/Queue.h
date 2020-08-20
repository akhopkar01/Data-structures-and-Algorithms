#pragma once
#include <vector>

class Queue
{
private:
	std::vector<int> vec;
public:
	void push(int&);
	int pop();
	bool is_empty();
	void display_queue();
};

