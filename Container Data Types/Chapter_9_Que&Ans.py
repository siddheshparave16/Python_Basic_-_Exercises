import operator

"""
Que C:- Answer the following



#Que b:- What will be the output of following code snippet ?

num1 = num2 = (10, 20, 30, 40, 50)
print(id(num1), type(num2))
print(isinstance(num1, tuple))
print(num1 is num2)
print(num1 is not num2)
print(20 in num1)
print(30 not in num2)


"""

"""
Que c:- Suppose a date is represented as a tuple (d, m, y). Write a program to create two date tuples and 
        find the number of days between two dates. 

# Answer starts here...


# Input: Get two dates from the user
print("Enter the first date:")
day1 = int(input("Day: "))
month1 = int(input("Month: "))
year1 = int(input("Year: "))

print("Enter the second date:")
day2 = int(input("Day: "))
month2 = int(input("Month: "))
year2 = int(input("Year: "))

# Store dates as tuples
date1 = (day1, month1, year1)
date2 = (day2, month2, year2)


# Days in each month (ignoring leap years for simplicity)
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Convert each date to the total number of days from the start of the year
def days_from_start_of_year(date):
    day, month, year = date
    total_days = sum(days_in_months[:month - 1]) + day
    return total_days

# Compare dates and calculate the difference in days element by element
if date1 > date2:
    diff_days = (
        (date1[2] - date2[2]) * 365 +  # Difference in years
        (date1[1] - date2[1]) * 30 +   # Difference in months (simplified to 30 days per month)
        (date1[0] - date2[0])          # Difference in days
    )
    print(f"The first date {date1} is later than the second date {date2}. Difference in days: {diff_days}")
elif date1 < date2:
    diff_days = (
        (date2[2] - date1[2]) * 365 +  # Difference in years
        (date2[1] - date1[1]) * 30 +   # Difference in months (simplified to 30 days per month)
        (date2[0] - date1[0])          # Difference in days
    )
    print(f"The second date {date2} is later than the first date {date1}. Difference in days: {diff_days}")
else:
    print(f"Both dates {date1} and {date2} are the same.")


"""

"""
Que d:- create a list of tuples. Each tuple should contain an item and its price in float. 
        Write a program to sort the tuples in descending order by price.
        
# Answer starts here..


# list of products name & price in tuple
products = [('Comb', 20.50), ('Pen', 50.20), ("Pencil", 25.60), ('Eraser', 10.30), ('Charger', 100.50)]

# print the list of tuple
print(products)

# let sort the tuples in descending order by price
sorted_products = sorted(products, key=operator.itemgetter(1))
print("List of Products in descending order by price :-\n", sorted_products)

  
"""

"""
Que e:- Store the data about shares held by a user as tuple containing the following information about shares:
        share name, date of purchase, cost price, number of shares, selling price.
        
        Write a program to determine :
        - Total cost of the portfolio.
        - Total amount gained or lost.
        - Percentage of profit made or loss incurred.


data = (
        ('Mrf', '2_April_2022', 500, 20, 650),
        ('Axis', '4_Jan_2024', 300, 15, 280),
        ('Paytm', '15_May_2024', 450, 30, 800),
        ('Tata', '12_Aug_2023', 600, 22, 480)
        )

# Initialize variables for portfolio totals
total_cost_portfolio = 0
total_selling_portfolio = 0


# Total cost of the portfolio
for s, _, cp, qty, sp in data:
    print(f"Shares :- {s}, Cost Price :- Rs.{cp}, Quantity :- {qty}, Selling Price :- Rs.{sp}")

    # Calculate cost and selling prices for the current share
    total_cost = cp * qty
    selling_cost = sp * qty

    # Update portfolio totals
    total_cost_portfolio += total_cost
    total_selling_portfolio += selling_cost

    # Calculate gain or loss for the current share
    if selling_cost > total_cost:
        profit = selling_cost - total_cost
        # Percentage of profit made
        profit_percentage = (profit / total_cost) * 100
        print(f"The Total Amount of gained from Shares {s} is Rs.{profit} ({profit_percentage:.2f}%)")

    elif total_cost > selling_cost:
        loss = total_cost - selling_cost
        # Percentage of profit made
        loss_percentage = (loss / total_cost) * 100
        print(f'The Total Amount of Loss from Shares {s} is Rs.{loss} and ({loss_percentage:.2f}%) ')

    else:
        print(f"No profit or loss for shares {s}.")

    print()

# Calculate portfolio-wide gain or loss
print("Portfolio Summary:")

if total_selling_portfolio > total_cost_portfolio:
    portfolio_profit = total_selling_portfolio - total_cost_portfolio
    portfolio_profit_percentage = (portfolio_profit/total_cost_portfolio) * 100
    print(f"Total portfolio profit: Rs.{portfolio_profit} ({portfolio_profit_percentage:.2f}%).")
elif total_cost_portfolio > total_selling_portfolio:
    portfolio_loss = total_cost_portfolio - total_selling_portfolio
    portfolio_loss_percentage = (portfolio_loss/total_cost_portfolio)*100
    print(f"Total Portfolio Loss: Rs.{portfolio_loss} ({portfolio_loss_percentage:.2f}%)")
else:
    print("No overall profit or loss in the portfolio.")

"""

"""
Que f:- Write a program to remove empty tuple from a list of tuples.

# Answer starts here..


# list of tuple
numbers = [(1, 2), (), (3,), (4, 5, 6), (), (), (8,), (), (9, 10)]
print('Original Numbers list :-',numbers)

# Initialize the filtered list
filter_numbers = []

# Filter out empty tuples
for tpl in numbers:
    # Check if tuple is non-empty
    if tpl:
        filter_numbers.append(tpl)

print('Filtered Numbers:', filter_numbers)

"""

"""

Que g:- Write a program to create following 3 lists.
        - a list of names
        - a list of roll numbers
        - a list of marks
        
        Generate and print a list of tuples containing name, roll numbers and marks from the 3 lists. 
        From this list generate 3 tuples - one containing all names, 
        another containing all roll numbers and third containing all marks.
"""

names = ['Jay', 'Yash', 'Vikas', 'Rashik']
roll_numbers = [101, 102, 103, 104]
marks = [85, 90, 95, 70]


# Generating a list of tuples containing name, roll number, and marks
combine_lst = []
for i in range(len(names)):
    combine_lst = combine_lst + [(names[i], roll_numbers[i], marks[i])]

print(combine_lst)


# Step 3: Generate three separate tuples - one for names, one for roll numbers, and one for marks
names_tpl = tuple(names)
roll_numbers_tpl = tuple(roll_numbers)
marks_tpl = tuple(marks)


# Print the results
print("Tuple of names:", names_tpl)
print("Tuple of roll numbers:", roll_numbers_tpl)
print("Tuple of marks:", marks_tpl)

