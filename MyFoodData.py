# Team: FoodDataMine
# Rosa Hulbert & Rasmane Sawadogo
# NETWORK DATABASES (SQL) Fall Quarter 2023 - CNE 340 – 12/03/2023
# WK12 - Final Project


import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from matplotlib import pyplot as plt

hostname = "127.0.0.1"
uname = "root"
pwd = ""
dbname = "fooddatamine"

# 12/01/23
# Create a connection to the MySQL database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

# 12/01/23
# Import MyFoodData from Download folder on my local machine
tables = pd.read_excel(r"C:\Users\Master_Ras\Downloads\MyFoodData.xlsx",sheet_name='Food',header=3)
# print(tables)

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
connection.close()

# Reading from table - Saving in df variable
df = pd.read_sql('SELECT * FROM my_food', engine)

grouped = df.groupby("Food Group")

fig, axes = plt.subplots(nrows = len(grouped), figsize = (10, 6 * len(grouped)))

# Looping to create each subplot
for i, (group_name, group_df) in enumerate(grouped):
    ax = axes[i] if len(grouped) > 1 else axes
    group_df.plot(x = "Fat (g)", y = "Calories", kind = "scatter", ax = ax, title = f"Food group: {group_name}")
    ax.set_xlabel("Fats in grams")
    ax.set_ylabel("Calories")

fig.tight_layout(pad = 15.0)
plt.show()


# USE NOTES FOR PRESENTATION # 12/02/23
# Import the necessary libraries
# Pandas --- It is used for manipulation
# sqlalchemy --- SQL toolkit and Object-relational Mapping library that provides a set of
# application programming Interface  for connecting relational databases.
# matplotlib.pyplot --- It is used for creating visualizations.