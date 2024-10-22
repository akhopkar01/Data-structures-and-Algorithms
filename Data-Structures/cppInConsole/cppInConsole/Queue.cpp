#include "Queue.h"
#include <iostream>

void Queue::push(int& data)
{
	vec.push_back(data);
}

int Queue::pop()
{
	int val = vec.front();
	vec.erase(vec.begin());
	return val;
}

bool Queue::is_empty()
{
	return vec.empty();
}

void Queue::display_queue()
{
	std::cout << "---Queue bottom---\n";
	for (const int& element : vec) {
		std::cout << "---" << element << "---\n";
	}
	std::cout << "---Queue Top---\n" << std::endl;
}
