import operator
import matplotlib.pyplot as plt


"""
Que :- Write a program that read a string from keyboard and
       creates dictionary containing frequency of each character occurring in the string.
       Also print these occurrences in the form of histogram.


# input string from user
input_string = input('Enter a string :- ')

# empty dictionary to store characters and their occurrence
char_dict = {}

# Counting character frequencies
for char in input_string:
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1

# Printing character frequencies
print("Character frequencies:", char_dict)

# Preparing data for the histogram
keys = list(char_dict.keys())
values = list(char_dict.values())

plt.bar(keys, values, color='skyblue')

# Adding labels and title
plt.xlabel('Characters')
plt.ylabel('Frequency')
plt.title('Character Frequency Histogram')

# Displaying the histogram
plt.show()

"""

"""
Que 2:- Create a dictionary contains names of students and marks obtain by them in three subjects.
        Write a program to replace the marks in three subjects with the total in three subjects,
        and average marks. Also report topper of the class.


# dictionary contains names of students and marks obtain by them in three subjects

students = {'Aman': {'sub1': 80, 'sub2': 75, 'sub3': 92},
            'Rajesh': {'sub1': 82, 'sub2': 70, 'sub3': 87},
            'Ajit': {'sub1': 68, 'sub2': 88, 'sub3': 95},
            'Vinit': {'sub1': 70, 'sub2': 82, 'sub3': 85},
            'Sunita': {'sub1': 85, 'sub2': 78, 'sub3': 82}
            }

topper = None
highest_total = 0

# total marks of three subjects and average marks
for name, subject in students.items():
    total_marks = sum(subject.values())
    avg_marks = total_marks / len(subject.values())

    # Update dictionary with total and average marks
    students[name] = {'Total': total_marks, 'Average': avg_marks}

    # Determine the topper
    if total_marks > highest_total:
        highest_total = total_marks
        topper = name


# Display the updated dictionary
print("Updated Student Records:")
for name, details in students.items():
    print(f"{name} : Total = {details['Total']}, Average = {details['Average']:.2f}")

# Report the topper of the class
print("\nTopper of the Class:")
print(f"{topper} with a Total of {highest_total} marks")


"""

"""
Que 3:- Given the following dictionary:

        write a program to perform the following operations:
        - Add a key to portfolio called 'MF' with values 'Relaince' and 'ABSL'
        - Set the value of 'accounts' to a list containing 'Axis' and 'BOB'.
        - sort the items in the list sorted under the 'shares' key.
        - Delete the list stored under 'ornaments' key.
         
# Answer starts here...

# Original portfolio dictionary
portfolio = {'accounts': ['SBI', 'IOB'],
             'shares': ['HDFC', 'ICICI', 'TM', 'TCS'],
             'ornaments': ['10 gm gold', '1 kg silver']
}


# Add a key to portfolio called 'MF' with values 'Relaince' and 'ABSL'
portfolio['MF'] = ['Relaince', 'ABSL']
print("After adding 'MF':", portfolio)

# Set the value of 'accounts' to a list containing 'Axis' and 'BOB'.
portfolio['accounts'] = ['Axis', 'BOB']
print("After updating 'accounts':", portfolio)

# sort the items in the list sorted under the 'shares' key.
portfolio['shares'].sort()
print("After sorting 'shares':", portfolio)


# Delete the list stored under 'ornaments' key.
if 'ornaments' in portfolio:
    del (portfolio['ornaments'])
print(portfolio)

"""

"""
Que 4:- Create two dictionaries - one containing grocery item and there price and
        another containing grocery items and quantity purchased. By using the values 
        from these two dictionaries compute the total bill.
        
# Answer starts from you.

# Dictionary contain Item and there Price
grocery_items = {'Rice': 50, 'Wheat': 40, 'Milk': 60, 'Eggs': 6, 'Sugar': 45, 'Salt': 20, 'Tea': 200, 'Oil': 150,
                 'Potatoes': 25, 'Tomatoes': 30, 'Onions': 40, 'Apples': 120, 'Bananas': 50, 'Chicken': 240,
                 'Fish': 300}


# Dictionary contain Item and there Quantity
grocery_items2 = {'Rice': 5, 'Wheat': 3, 'Milk': 2, 'Eggs': 12, 'Sugar': 1, 'Salt': 1, 'Tea': 0.5, 'Oil': 2,
                  'Potatoes': 2, 'Tomatoes': 1.5, 'Onions': 1, 'Apples': 2, 'Bananas': 12, 'Chicken': 1.5, 'Fish': 1}


# Initialize total amount
total_amount = 0

# Calculate the total bill
print("Item-wise Billing Details:")
for item in grocery_items.keys():
    item_total = grocery_items[item] * grocery_items2[item]
    print(f"{item}: {grocery_items[item]} x {grocery_items2[item]} = {item_total}")
    total_amount += item_total

# Print total bill amount
print(f'\nTotal Amount of bill purchase is {total_amount}.')


"""

"""
Que 5:- Which function will use to fetch all keys, all values and key value pairs from a given dictionary ?
 

grocery_items = {'Rice': 50, 'Wheat': 40, 'Milk': 60, 'Eggs': 6, 'Sugar': 45, 'Salt': 20, 'Tea': 200, 'Oil': 150}

# fetch all keys
print("keys :", grocery_items.keys())

# fetch all values
print("Values :", grocery_items.values())


# fetching all key value pair
for k, v in grocery_items.items():
    print(k, v)

"""

"""
Que 6:- Create a dictionary of 10 usernames and passwords. Receive the username and password from keyboard
        and search for them in the dictionary. Print appropriate message on the screen based on whether a
        match is found or not.


user_credentials = {
    'user1': 'password123', 'user2': 'securePass456', 'user3': 'welcome789',
    'user4': 'passkey321', 'user5': 'admin2024', 'user6': 'guest098',
    'user7': 'mySecret007', 'user8': 'lockItUp555', 'user9': 'hiddenPass901', 'user10': 'unlockMe111'
    }

# Receive username and password from the user
username, password = input('Enter Username and Password (separated by a colon ":"):').split(':')
print(f"Username: {username}, Password: {password}")


# Check if username exists and the password matches
if username in user_credentials.keys():
    if password == user_credentials[username]:
        print(f'{username} match for {password}, User Found')
    else:
        print("Incorrect password. Match not Found.")
else:
    print("Username not found. Match not Found.")

"""

"""
Que 7:- Given following dictionary

        write a program to perform the following operations :
        - Print marks obtained by Amol in English.
        - Set marks obtained by Raka in Maths to 77.
        - Sort the dictionary by name.
        


marks = {
         'Subu': {'Maths': 88, 'Eng': 60, 'Sst': 95},
         'Amol': {'Maths': 78, 'Eng': 68, 'Sst': 89},
         'Raka': {'Maths': 56, 'Eng': 66, 'Sst': 77}
        }


# Print marks obtained by Amol in English.
amol_english_marks = marks['Amol']['Eng']
print("Marks obtained by Amol in English:", amol_english_marks)

# Set marks obtained by Raka in Maths to 77.
marks['Raka']['Maths'] = 77
print("\nUpdated Marks Dictionary:")
print(marks)

# Sort the dictionary by name.
marks_sorted = sorted(marks.items())
print("\nSorted Dictionary by Name:")
print(marks_sorted)


"""

"""
Que 8:- Create a dictionary which stores the following data:

    Interface  IP Address   Status
    eth0        1.1.1.1     up
    eth1        2.2.2.2     up
    wlan0       3.3.3.3     down
    wlan1       4.4.4.4     up

Write a program to form a following operations:
- Find the status of a given Interface.
- Find Interface and IP of all Interface which are up.
- Find the total number of Interface.
- Add two new entries to the dictionary.




Interface = {
              'eth0': {'IP Address': '1.1.1.1', 'Status': 'up'},
              'eth1': {'IP Address': '2.2.2.2', 'Status': 'up'},
              'wlan0': {'IP Address': '3.3.3.3', 'Status': 'down'},
              'wlan1': {'IP Address': '4.4.4.4', 'Status': 'up'}
            }


# Find the status of a given Interface.
print("Status of Interface in Dictionary are :- ")
for k, v in Interface.items():
    print(f"Interface :{k}, Status: {v['Status']}")

print()

# Find Interface and IP of all Interface which are up.
print("Interface & IP Address which status is 'up':")
for k, v in Interface.items():
    if v['Status'] == 'up':
        print(f"Interface: {k},Status: {v['IP Address']}")


# Find the total number of Interface.
total_interfaces = len(Interface)
print(f'\nTotal Number of Interface in Dictionary is :{total_interfaces}\n')


# Add two new entries to the dictionary.

Interface['eth3'] = {'IP Address': '5.5.5.5', 'Status': 'down'}
Interface['wlan2'] = {'IP Address': '6.6.6.6', 'Status': 'up'}


# Display the updated dictionary
print("Updated Interfaces dictionary:")
for interface, details in Interface.items():
    print(f"Interface: {interface}, IP Address: {details['IP Address']}, Status: {details['Status']}")


"""

"""
Que 9:- Suppose a dictionary contain 5 key-value pair of name and marks.
        write a program to print them from the last pair to first pair.
        Keep deleting every pair printed, such that the end of printing the falls empty. 
"""

students = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'Diana': 92, 'Ethan': 88}

# printing from last to first

while students:
    last_item = students.popitem()
    print(f'{last_item}')


print(students)



d = {
     'd1': {'Fruitname': 'Mango', 'Season': 'Summer'},
     'd2': {'Fruitname': 'Orange', 'Season': 'Winter'}
    }

print(d['d1']['Fruitname'])
print(d['d2']['Season'])


"""
Que :- what is the most common usage of the data types mentions below ? 

1. List - Used for storing an mutable ordered collection of items
2. Tuple - Storing immutable ordered collections of items.
3. set - Storing unique, unordered items. Often used for membership tests or removing duplicates.
4. Dictionary - Storing key-value pairs, allowing fast lookups, updates, and deletions based on a key.
5. String - Storing and manipulating text data.

"""


