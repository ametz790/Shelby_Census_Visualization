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

    db_cursor.execute('select Label, Percent from gross_rent;')
    result = db_cursor.fetchall


# gross_rent table
    Label = []
    Percent = []


    for r in db_cursor:
        Label.append(r[0])
        Percent.append(r[1])


    x_label = np.array(Label)[2:-2]
    y_per = np.array(Percent)[2:-2]

#####

    y_per = [i.strip('%') for i in y_per]
    y_per = np.asarray(y_per, dtype=float)
#####

    fig, ax2 = plt.subplots()


    ax2.barh(x_label,y_per)
    ax2.xaxis.set_major_formatter(mtick.PercentFormatter())

    plt.ylabel("Gross Rent")
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