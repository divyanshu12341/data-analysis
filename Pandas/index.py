import pandas as pd
data = {
     "day":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
     "Sales":[100,120,110,130,150,160,170] }
df = pd.DataFrame(data) 
print(df)

# Each key becomes a column
# Each row is one observation
# DataFrame = labeled table

# Accessing sales
print(df["Sales"])
print(df[["day","Sales"]])

# Mini-exercise Create a DataFrame with:
# 5 days
# 5 expense values
# Print:
# The entire DataFrame
# Only the expense column

five_days = {
    "days":["Mon","Tue","Wed","Th","Fr"],
    "expense_values":[100,101,200,201,301]
}
df = pd.DataFrame(five_days)
print(df)
print(df["expense_values"])

df = pd.read_csv("expenses.csv")

# it prints first 3 rows
print(df.head(3))

# column names
print(df.columns)

# Shape
print(df.shape)
# Now we learn how to 
# 1) Inspect bad columns 
# 2) Remove useless data 
# 3) validate structure 

# To inspect structure 
df.info()
# It tells -> 
# 1) Column-names 
# 2) non-null counts 
# 3) Data types 

# Conceptually,columns with all null values are meaningless and 
# it should be removed 

# Empty or meaningless columns are dangerous because they can break 
# calculations, distort aggregations, confuse visualizations, and
#  mislead analysis.

# this returns only rows meeting the condition  
df[df["Expense"]>150]

df[(df["Expense"]>120) & (df["Expense"]<180)]

# Using your expenses.csv DataFrame:
# Filter and print days where expense is greater than 140
# Count how many such days exist

df[df["Expense"]>140]
count = 0
counts  = df["Expense"]>140
for i in counts:
    if i == True:
        count = count+1
print(count)

