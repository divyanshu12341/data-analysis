print('Python is working')

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

# Mini-exercise:
# Write code to:
# Create two variables: total_sales = 1250 and days = 7
# Compute average daily sales
# Print the result

total_sales = 1250
days = 7
avg_daily_sales = (total_sales)/(days)
print(avg_daily_sales)

if avg_daily_sales>200:
    print("High sales")
else:
    print("Normal sales")


#Write code that:
#Stores a variable score
#Prints:
#"Pass" if score ≥ 40
#"Fail" otherwise

score = 100
if score>=40:
    print("Pass")
else:
    print("Fails")
