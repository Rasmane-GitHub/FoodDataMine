# USE NOTES FOR PRESENTATION # 12/01/23

# Import the necessary libraries
# Pandas --- It is used for manipulation
# openpyxl --- It is used for handling Excel files
# sqlalchemy --- SQL toolkit and Object-relational Mapping library that provides a set of
# application programming Interface  for connecting relational databases.
# matplotlib.pyplot --- It is used for creating visualizations.

import pandas as pd
import openpyxl
import xlrd
from fontTools.varLib import plot

from sqlalchemy import create_engine
from sqlalchemy import text
import pymysql

from matplotlib import pyplot as plt
# Or import matplotlib.pyplot as plt

hostname = "127.0.0.1"
uname = "root"
pwd = ""
dbname = "fooddatamine"

# 12/01/23
# Create a connection to the MySQL database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(host=hostname, db=dbname, user=uname, pw=pwd))

# 12/01/23
# Import MyFoodData from Download folder on my local machine
tables = pd.read_excel(r"C:\Users\Master_Ras\Downloads\MyFoodData.xlsx",
                       sheet_name='Food',
                       header=3)
print(tables)

# 12/01/23
# Connect to the database and store the data from tables into temporary table (temp_food)
connection = engine.connect()
tables.to_sql('temp_food', con=engine, if_exists='append')

# 12/01/23
# Create a new table (my_food) with the same structure as temp_food, then insert the data from temp_food into my_food.
# Drop the temporary table (temp_food)
# Close the database connection
connection.execute(text('CREATE TABLE my_food like temp_food'))
connection.execute(text('INSERT INTO my_food(ID, name, `Food Group`, Calories, `Fat (g)`, `Protein (g)`, `Carbohydrate (g)`, `Sugars (g)`) SELECT DISTINCT ID, name, `Food Group`, Calories, `Fat (g)`, `Protein (g)`, `Carbohydrate (g)`, `Sugars (g)` FROM temp_food'))
connection.execute(text('DROP TABLE temp_food'))
connection.close()  # Close extension to database


######################################################################################################################

# NEW CODE 11/30/23
data = ['my_food']

# 12/01/23
# Create dataFrame with column names
df = pd.DataFrame(data, columns=['ID', 'name', 'Food Group', 'Calories', 'Fat', 'Protein', 'Carbohydrate', 'Sugars'])
print(df)

# df = pd.read_sql_table('my_food', engine.connect()) -
# print(df) -

df.plot(x='Waffle Plain Frozen Ready-To-Heat Microwave', y='Calories')
plt.xlabel('Waffle Plain Frozen Ready-To-Heat Microwave')
plot.ylabel('Calories')
plt.title('Waffle Plain Frozen Ready-To-Heat Microwave', 'Calories')
plot.show()

# df.plot(x='Waffle Plain Frozen Ready-To-Heat Microwave', y='Calories')
# plt.xlable('Waffle Plain Frozen Ready-To-Heat Microwave')
# plot.ylabel('Calories')
# plt.tile('Waffle Plain Frozen Ready-To-Heat Microwave', 'Calories')
# plot.show()

# NEW
# plt.figure(figsize=(10, 6))
# plt.bar(df['name'], df['Calories'])
# plt.xlabel('Food Items')
# plt.ylabel('Calories')
# plt.title('Calories in Food Items')
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()

plt.figure(figsize=(6, 6))
plt.bar(df['Calories'], df['sugar'])
plt.bar(df['name'], df['Calories'])
plt.xlabel('Food Name')
plt.xticks(rotation=90)
plt.ylabel('Calories')
plt.title('Calories in Foods')
plt.show()

connection.close()
#Rasy and Rosa