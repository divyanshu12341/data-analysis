# print('Python is working')

age = 23
height = 5.9
name = "Divyanshu"
is_student = True

print(age)
print(height)
print(name)
print(is_student)

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

a = 10
b = 3
print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # results float
print(a//b) # floor-division
print(a%b) #remainder

# # Mini-exercise:
# # Write code to:
# # Create two variables: total_sales = 1250 and days = 7
# # Compute average daily sales
# # Print the result

total_sales = 1250
days = 7
avg_daily_sales = (total_sales)/(days)
print(avg_daily_sales)

if avg_daily_sales>200:
    print("High sales")
else:
    print("Normal sales")


# #Write code that:
# #Stores a variable score
# #Prints:
# #"Pass" if score ≥ 40
# #"Fail" otherwise

score = 100
if score>=40:
    print("Pass")
else:
    print("Fails")

for i in range(5):
    print(i)

# #Mini-exercise
# #Write code that:
# #Prints all even numbers from 1 to 20

for i in range(1,21):
    if i%2 ==0:
        print(i)

# # Mini-Project: Weekly Expense Analyzer
# # Task
# # Write a Python program that:
# #Stores 7 daily expenses (hard-coded values are fine)
# #Uses a loop to calculate:
# #Total expense
# #Average expense
# #Prints both results
# #Constraints
# #Use variables
# #Use a for loop
# #Do not use any libraries yet

daily_expense_1 = 100


total = 0
for i in range(7):
    total += daily_expense_1
print(total)
avg = total/7
print(avg)

# # List is an ordered collection of values
# #Conceptually,one variable that is loopable and analyzable

# # Square brackets [] define a list

# # Order matters

# # All expenses live under one variable
daily_expenses = [100,150,200,80,120,90,60]
print(daily_expenses)
print(type(daily_expenses))

# # Accessing elements

# # Accessing first element
print(daily_expenses[0])

# # Accesing seventh element
print(daily_expenses[6])


# # Looping over a list
total = 0
# for expense in daily_expenses:
    total+=expense

print(total)
print(total/len(daily_expenses))

# # Mini-exercise
# # Create a list of 5 numbers
# # Loop through it and print each value

num = [1,3,5,7,9]
for numbers in num:
    print(numbers)

# # Learn how to:
# # Add values
# # Measure size
# # Compute aggregates

expenses = [100,200,150]
expenses.append(250)
print(expenses)

print(len(expenses)) # no of all records in expenses
print(sum(expenses)) # sum of all elements in expenses
print(max(expenses)) # max of all elements in expenses
print(min(expenses)) # min of all elements in expenses

# Using a list of daily expenses:
# Calculate total expense
# Calculate average expense
# Print both with clear meaning
total_expense = sum(expenses)
no_of_expenses = len(expenses)
average_expenses = total_expense/no_of_expenses
print("Total expense are ",total_expense)
print("Average expenses are ",average_expenses)

# Our above code assumes:
# expenses already exists
# It is non-empty
# Later, when we read CSV files, empty data will break averages.
# This is why validation becomes important.

# Dictionary
student_marks = {
    "Amit": 78,
    "Ravi": 85,
    "Neha": 92
}
print(student_marks)
print(student_marks["Neha"])
# Keys ("Amit") act like labels
# Values (78) are the data
# Access is by meaning, not position

for name,marks in student_marks.items():
    print(name,marks)

# Mini-exercise
# Create a dictionary that:
# Stores 5 students and their marks
# Loops through it
# Prints only students who scored above 80

student_details = {
    "Divyanshu":95,
    "Amit": 91,
    "Divyesh":89,
    "Devesh": 86,
    "Ankit": 87
}
for name,marks in student_details.items():
    if(marks>80):
        print("Student name: ",name," Marks: ",marks)
