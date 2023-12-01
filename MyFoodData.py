import pandas as pd
import openpyxl
import xlrd

from sqlalchemy import create_engine
from sqlalchemy import text
import pymysql

from matplotlib import pyplot as plt

# Or import matplotlib.pyplot as plt

hostname = "127.0.0.1"
uname = "root"
pwd = ""
dbname = "fooddatamine"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(host=hostname, db=dbname, user=uname, pw=pwd))
# Import MyFoodData website address
tables = pd.read_excel(r"C:\Users\Master_Ras\Downloads\MyFoodData.xlsx",
                       sheet_name='Food',
                       header=3)
print(tables)

connection = engine.connect()
tables.to_sql('temp_food', con=engine, if_exists='append')

connection.execute(text('CREATE TABLE my_food like temp_food'))
connection.execute(text(
    'INSERT INTO my_food(ID, name, `Food Group`, Calories, `Fat (g)`, `Protein (g)`, `Carbohydrate (g)`, `Sugars (g)`) SELECT DISTINCT ID, name, `Food Group`, Calories, `Fat (g)`, `Protein (g)`, `Carbohydrate (g)`, `Sugars (g)` FROM temp_food'))
connection.execute(text('DROP TABLE temp_food'))
connection.close()  # Close extension to database

# New code 11/30/23
data = ['my_food']
df = pd.read_sql_table('my_food', engine.connect())
print(df)
df.plot(x='Waffle Plain Frozen Ready-To-Heat Microwave', y='Calories')
plt.xlable('Waffle Plain Frozen Ready-To-Heat Microwave')
plot.ylabel('Calories')
plt.tile('Waffle Plain Frozen Ready-To-Heat Microwave', 'Calories')
plot.show()
# print(df)
#
# plt.figure(figsize=(24, 24))
# plt.plot(df['Date'], df['Diesel_Price'])
# plt.xlabel('Date')
# plt.xticks(rotation=90)
# plt.ylabel('Open')
# plt.title('Diesel Over Time', fontsize=16)
# plt.show()
#


# WRITE YOUR NEW CODE HERE
# DATA

# plt.plot(temp_food.ID, MyFoodData.name)
# plot.show()
#
# plt.figure(figsize=(6, 6))
# plt.bar(df['Calories'], df['sugar'])
# plt.bar(df['name'], df['Calories'])
# plt.xlabel('Food Name')
# plt.xticks(rotation=90)
# plt.ylabel('Calories')
# plt.title('Calories in Foods')
# plt.show()

# connection.close()
