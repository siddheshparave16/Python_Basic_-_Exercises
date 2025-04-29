import json

from django.utils.lorem_ipsum import paragraph, words

"""
Que 1:- Write a program to read a file and display its contents along with
        line numbers before each line.

# Answer starts here...

with open('messages.txt', 'r') as f:
    # display its contents along with line numbers
    for index, data in enumerate(f):
        print(index, data)

"""


"""
Que 2:- Write a program that append a content of one file at end of another.

# Answer starts here...


source_file = input("Enter the name of the source file to append from: ")
destination_file = input("Enter the name of the destination file to append to: ")

with open(destination_file, 'a') as f1:

    try:
        with open(source_file, 'r') as f2:
            for data in f2:
                f1.write(data)
    except FileNotFoundError:
        print(f"The file {source_file} does not exist. Please check the file name and try again.")

with open('messages2.txt', 'r') as f1:
    for data in f1:
        print(data)

"""


"""
Que 3:- Suppose the file contains student's records with each record containing name and age of student.
        Write a program to read this records and display them in sorted order by name.



with open('students', 'w+') as f:
    lst = students = [{'name': 'John', 'age': 20}, {'name': 'Alice', 'age': 22}, {'name': 'Bob', 'age': 19}]

    # serialization of data
    json.dump(lst, f)

    # moving cursor at beginning of file
    f.seek(0)

    # deserialization of date
    students_data = json.load(f)
    print(students_data)
    sorted_students = sorted(students_data, key=lambda x: x['name'])

    # Printing sorted student names and their details
    print('Students in sorted order by name:')

    for student in sorted_students:
        print(f"Name: {student['name']}, Age: {student['age']}")


"""


"""
Que 4:- Write a program to copy contents of one file to another. 
        While doing so replace all lowercase characters with their equivalent uppercase characters.   



with open('messages2.txt', 'a+') as f1:
    with open('messages.txt', 'r') as f2:
        for data in f2:
            f1.write(data.upper())


    # Moving cursor back to the beginning at file f1.
    f1.seek(0)
    for data in f1:
        print(data)

"""


"""
Que 5:- Write a program that mergers lines alternately from two files and write a results
        If one file has a smaller number of lines than the other, the remaining lines from
        larger should be simply copied into the target file. 

# Answer starts here..

with open('Quotes', 'a+') as output_file, open('Content1.txt', 'r') as f1, open('Content2.txt', 'r') as f2:
    # read all lines from each file and form a list of lines
    line1 = f1.readlines()
    line2 = f2.readlines()

    for line1, line2 in zip(line1, line2):
        # strip() is used to remove any extra spaces or newline characters from each line.
        output_file.write(line1.strip() + " " + line2)


"""


"""
Que 6:- Suppose an Employee object contain following details:
        employee code, employee name, date of joining, salary.
        write a program to serialize and deserialize the data.


# Employee details
employee1 = {'Code': 'A102', 'Name': 'Ajit', 'Date_of_joining': '12/07/2023', 'Salary': 15600}

# Serialize the employee data into JSON string
emp_data = json.dumps(employee1)

# Deserialize the JSON string back into a Python dictionary
get_emp_data = json.loads(emp_data)

# Print the deserialized data and its type
print(get_emp_data)
print(type(get_emp_data))


"""


"""
Que 7:- A hospital keep file of blood donors in which each record has the format:
        Name: 20 columns, Address = 40 columns, Age = 2 Columns, Blood type: 1 column(Type 1,2,3 or 4).
        
        Write a program to read the file and print a list of all blood donors 
        whose age is below 25 and whose blood type is 2.

# Answer starts here..


with open('Blood_Donors_Data', 'w') as f1:
    blood_donors = [
        {'Name': 'John Doe', 'Address': '123 Elm Street, Springfield, IL', 'Age': 25, 'Blood Type': '1'},
        {'Name': 'Alice Smith', 'Address': '456 Oak Avenue, Chicago, IL', 'Age': 20, 'Blood Type': '2'},
        # Age < 25, Blood Type 2
        {'Name': 'Bob Brown', 'Address': '789 Maple Drive, Naperville, IL', 'Age': 28, 'Blood Type': '3'},
        {'Name': 'Carol White', 'Address': '101 Pine Lane, Evanston, IL', 'Age': 22, 'Blood Type': '4'},
        {'Name': 'David Black', 'Address': '555 Birch Road, Lincolnshire, IL', 'Age': 19, 'Blood Type': '2'},
        # Age < 25, Blood Type 2
        {'Name': 'Emma Green', 'Address': '202 Cedar Blvd, Oak Park, IL', 'Age': 29, 'Blood Type': '2'},
        {'Name': 'Frank Lee', 'Address': '678 Ash Dr, Skokie, IL', 'Age': 24, 'Blood Type': '3'},
        {'Name': 'Grace King', 'Address': '233 Walnut St, Downers Grove, IL', 'Age': 35, 'Blood Type': '4'},
        {'Name': 'Helen White', 'Address': '156 Birchwood Ln, Wheaton, IL', 'Age': 23, 'Blood Type': '1'},
        {'Name': 'Ivan Black', 'Address': '420 Maplewood Rd, Aurora, IL', 'Age': 18, 'Blood Type': '2'},
        # Age < 25, Blood Type 2
        {'Name': 'Jack Red', 'Address': '99 Oakwood Rd, DeKalb, IL', 'Age': 33, 'Blood Type': '3'},
        {'Name': 'Karen Grey', 'Address': '500 Pine St, Joliet, IL', 'Age': 26, 'Blood Type': '4'},
        {'Name': 'Leo Tan', 'Address': '1500 Birch St, Palatine, IL', 'Age': 21, 'Blood Type': '2'},
        # Age < 25, Blood Type 2
        {'Name': 'Mia Evans', 'Address': '788 Chestnut Ln, Libertyville, IL', 'Age': 22, 'Blood Type': '2'},
        # Age < 25, Blood Type 2
        {'Name': 'Noah Fisher', 'Address': '232 Aspen Dr, Glenview, IL', 'Age': 28, 'Blood Type': '3'},
        {'Name': 'Olivia Harris', 'Address': '555 Redwood St, Hinsdale, IL', 'Age': 34, 'Blood Type': '4'},
        {'Name': 'Peter Clark', 'Address': '300 Willow Rd, Berwyn, IL', 'Age': 26, 'Blood Type': '1'},
        {'Name': 'Quinn Young', 'Address': '48 Cedar Rd, Elgin, IL', 'Age': 25, 'Blood Type': '2'},
        # Age < 25, Blood Type 2
        {'Name': 'Rachel Morgan', 'Address': '900 Oak St, Batavia, IL', 'Age': 24, 'Blood Type': '3'},
        {'Name': 'Steven Martin', 'Address': '1201 Pine Ave, Mount Prospect, IL', 'Age': 23, 'Blood Type': '4'},
        # Age < 25, Blood Type 2
        {'Name': 'Tina Scott', 'Address': '712 Cedar St, Schaumburg, IL', 'Age': 23, 'Blood Type': '1'},
        {'Name': 'Uriel Foster', 'Address': '823 Maple Ave, Highland Park, IL', 'Age': 20, 'Blood Type': '2'},
        # Age < 25, Blood Type 2
        {'Name': 'Vanessa Green', 'Address': '634 Pine Dr, Arlington Heights, IL', 'Age': 22, 'Blood Type': '3'},
        {'Name': 'William Clark', 'Address': '145 Willow Ave, Oak Brook, IL', 'Age': 29, 'Blood Type': '4'}
    ]

    # Serialize a data into JSON string to store in file
    json.dump(blood_donors, f1)


# print a list of all blood donors whose age below 25 and blood type 2.


# Open the 'Blood_Donors_Data' file in read mode to load donor information
with open('Blood_Donors_Data', 'r') as f:

    # Load the JSON data (list of dictionaries) from the file
    data = json.load(f)

    # Print the loaded data and its type (for debugging or understanding the structure)
    print(data)
    print(type(data))

    # Using for loop
    # donors_type2 = []
    # for d in data:
    #     if d['Age'] < 25 and d['Blood Type'] == '2':
    #         donors_type2.append(d)

    # Filter donors using list comprehension:
    # 1. Age should be less than 25 and 2. Blood Type should be '2'
    # The result will be a new list of donors meeting both conditions

    donors_type2 = [donor for donor in data if donor['Age'] < 25 and donor['Blood Type'] == '2']

    # Print the filtered list of donors who are under 25 and have blood type '2'
    print(donors_type2)
    print(f"Count of Donors whose Age is below 25 and Blood Type '2' are {len(donors_type2)}.")


"""

"""
Que 8:- Given list of names of students in a class. write a program to store the names in file on disk.
        Make a provision to display the nth name in the list, where n is read from keyboard.
        
# Answer starts here...


students = [
    "John Doe", "Alice Smith", "Bob Brown", "Carol White", "David Black",
    "Emma Green", "Frank Lee", "Grace King", "Helen White", "Ivan Black",
    "Jack Red", "Karen Grey", "Leo Tan", "Mia Evans", "Noah Fisher",
    "Olivia Harris", "Peter Clark", "Quinn Young", "Rachel Morgan", "Steven Martin"
]


with open('students', 'w+') as f:
    # serialize data and store in file
    json.dump(students, f)

    # Move file cursor to the beginning
    f.seek(0)

    # Load the JSON data into a list
    data = json.load(f)
    print(data)

    # Get user input
    student_no = int(input('Enter a Integer place to get student at that place:- '))

    # Validate the input and retrieve the student name
    if 1 <= student_no <= len(data):
        print(f"The student at position {student_no} is: {data[student_no - 1]}")
    else:
        print("Invalid position! Please enter a number between 1 and", len(data))


"""


"""
Que 9:- Assume that a Master File contains two field, roll number and name of student.
        At the end of the year, a set of students join a class and another set leaves. 
        A transaction file contains the roll number and an appropriate code to add or delete a student.
        
        Write a program to create another file that contains the updated list of names and roll numbers. 
        Assume that the Master file and the transaction file are arranged in ascending order by roll numbers.
        The updated file should also be in ascending order by roll numbers. 

# Answer starts here..


students = [
    {"roll_no": 101, "name": "Aryan Sharma"},
    {"roll_no": 102, "name": "Kavya Mehta"},
    {"roll_no": 103, "name": "Aditya Singh"},
    {"roll_no": 104, "name": "Neha Gupta"},
    {"roll_no": 105, "name": "Rohan Verma"},
    {"roll_no": 106, "name": "Priya Desai"},
    {"roll_no": 107, "name": "Sarthak Jain"},
    {"roll_no": 108, "name": "Ananya Roy"},
    {"roll_no": 109, "name": "Ishaan Patel"},
    {"roll_no": 110, "name": "Sneha Das"}
]

# creating the master file
with open('Master_File.txt', 'w') as mf:
    # Serialize data and store in file.
    json.dump(students, mf)


# transaction file.

students_transaction_data = [
    {"roll_no": 102, "name": "Kavya Mehta", 'code': 'add'},
    {"roll_no": 103, "name": "Aditya Singh", 'code': 'delete'},
    {"roll_no": 104, "name": "Neha Gupta", 'code': 'delete'},
    {"roll_no": 105, "name": "Ajit Rathod", 'code': 'add'},
    {"roll_no": 107, "name": "Rohan Verma", 'code': 'add'}
]


# creating the transaction file
with open('Transaction_file.txt','w') as tf:
    # serialize data and store in file
    json.dump(students_transaction_data, tf)

# file that contains the updated list of names and roll numbers.

with open('Master_File.txt', 'r') as mf, open('Transaction_file.txt', 'r') as tf:
    master_data = json.load(mf)
    transaction_data = json.load(tf)

    # Convert master_data into a dictionary for easier processing by roll number
    master_dict = {student['roll_no']: student for student in master_data}

    # process each transaction
    for t_data in transaction_data:
        roll_no = t_data['roll_no']

        if t_data['code'] == 'add':
            # Only add if the student is not already in the Master File
            if roll_no not in master_dict:
                # Add new student
                master_dict[roll_no] = { 'roll_no': t_data['roll_no'], 'name': t_data['name']}
        elif t_data['code'] == 'delete':
            # Delete the student if they exist in the Master File
            if roll_no in master_dict:
                # Remove student
                del master_dict[roll_no]


    # After processing all transactions, update the list
    updated_list = list(master_dict.values())
    print(updated_list)


# Write the updated list back to the file
with open('Updated_students.txt','w') as uf:
    # Convert each student record to JSON and write to file
    for student in updated_list:
        uf.write(json.dumps(student) + '\n')


"""


"""
Que 10:- Given a text file, write a program to create another text file
         deleting the words "a", "the", "an" and replace each one of them with a blank space.
"""

with open('textfile.txt', 'w') as tf:
    para = ("She is reading a book about the history of technology. The team has an innovative approach to "
            "solving problems. They are working on a project that will change the future of the industry."
            " The company has a vision to revolutionize the way we use technology in everyday life.")
    tf.write(para)


with open('updated_textfile.txt', 'w') as uf, open('textfile.txt', 'r') as tf:

    # read all data from file
    data = tf.read()
    # create a list of words
    words_in_data = data.split()

    # check condition
    for word in words_in_data:
        # replace ['a', 'an', 'the'] with blank space
        if word.lower() in ['a', 'an', 'the']:
            uf.write('' + ' ')
        else:
            # if word in not in ['a', 'an', 'the'] add word at it is.
            uf.write(word + ' ')



