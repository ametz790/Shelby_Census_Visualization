import mysql
import pandas as pd
import mysql.connector as sql
import matplotlib
import PyQt5
import matplotlib.ticker as mtick
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
import matplotlib.axes
import numpy as np
from mysql.connector import errorcode

try:
    db_connection = mysql.connector.connect(user='***', password='***',
                              host='***',
                              database='shelby_census')
    db_cursor = db_connection.cursor()

    db_cursor.execute('select Column_1,Households, Families, Married_couple_families, Nonfamily_households from income')
    result = db_cursor.fetchall

    Column_1 =[]
    Households = []
    Families = []
    Married_couple_families=[]
    Nonfamily_households=[]

    for i in db_cursor:
        Column_1.append(i[0])
        Households.append(i[1])
        Families.append(i[2])
        Married_couple_families.append(i[3])
        Nonfamily_households.append(i[4])

    x_income = np.array(Column_1)[2:-2]
    y_house = np.array(Households)[2:-2]
    y_fam = np.array(Families)[2:-2]
    y_married = np.array(Married_couple_families)[2:-2]
    y_nonfam = np.array(Nonfamily_households)[2:-2]

#####
    y_house = [i.strip('%') for i in y_house]
    y_house=np.asarray(y_house,dtype=float)

    y_fam = [i.strip('%') for i in y_fam]
    y_fam = np.asarray(y_fam, dtype=float)

    y_married = [i.strip('%') for i in y_married]
    y_married = np.asarray(y_married, dtype=float)

    y_nonfam = [i.strip('%') for i in y_nonfam]
    y_nonfam = np.asarray(y_nonfam, dtype=float)
#####

    fig, ax = plt.subplots()

    ax.barh(x_income, y_house, label='Household')
    ax.barh(x_income, y_fam, left=y_house, label='Family')
    ax.barh(x_income, y_married, left=y_house + y_fam, label='Married')
    ax.barh(x_income, y_nonfam, left=y_house + y_fam + y_married, label='Non-Family')

    plt.xticks(range(0,95,5))
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())

    plt.ylabel("Income")
    plt.xlabel("Percentages")
    plt.legend()

    plt.show()

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    db_connection.close()