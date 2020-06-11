

def smallest_positive(arr):
    # Find the smallest positive number in the list
    min = None
    for num in arr:
        if num > 0:
            if min == None or num < min:
                min = num
    return min

def when_offered(courses, course):
    output = []
    for semester in courses:
        for course_names in courses[semester]:
            if course_names == course:
                output.append(semester)
    return output

if __name__ == "__main__":
    choice = int(input("Which Program to execute? Smallest Positives (1) OR Offered Semester (2) [Numeric entry] "))
    if choice == 1:
        testcases = dict(test1= [4, -6, 7, 2, -4, 10], test2= [.2, 5, 3, -.1, 7, 7, 6], test3= [-6, -9, -7], test4= [], test5= [88.22, -17.41, -26.53, 18.04, -44.81, 7.52, 0.0, 20.98, 11.76])
        for key in testcases:
            print("Output for {} : {}". format(key,smallest_positive(testcases[key])))
    if choice == 2:
        courses = {
            'spring2020': {'cs101': {'name': 'Building a Search Engine',
                                     'teacher': 'Dave',
                                     'assistant': 'Peter C.'},
                           'cs373': {'name': 'Programming a Robotic Car',
                                     'teacher': 'Sebastian',
                                     'assistant': 'Andy'}},
            'fall2020': {'cs101': {'name': 'Building a Search Engine',
                                   'teacher': 'Dave',
                                   'assistant': 'Sarah'},
                         'cs212': {'name': 'The Design of Computer Programs',
                                   'teacher': 'Peter N.',
                                   'assistant': 'Andy',
                                   'prereq': 'cs101'},
                         'cs253': {'name': 'Web Application Engineering - Building a Blog',
                                   'teacher': 'Steve',
                                   'prereq': 'cs101'},
                         'cs262': {'name': 'Programming Languages - Building a Web Browser',
                                   'teacher': 'Wes',
                                   'assistant': 'Peter C.',
                                   'prereq': 'cs101'},
                         'cs373': {'name': 'Programming a Robotic Car',
                                   'teacher': 'Sebastian'},
                         'cs387': {'name': 'Applied Cryptography',
                                   'teacher': 'Dave'}},
            'spring2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                                     'teacher': 'Dorina'},
                           'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                                     'teacher': 'Jasper'},
                           }
        }

        testcase = dict(test1= 'cs101', test2= 'bio893')
        for key in testcase:
            print("Output for {}: {}".format(key,when_offered(courses, testcase[key])))