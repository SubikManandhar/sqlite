import sqlite3
import json
import requests
import sys

response = requests.get("https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json")
data_json=response.json()
sqliteConnection = sqlite3.connect('SQLite_Python.db')
cursor = sqliteConnection.cursor()
try:

    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS tableyipl (
                                    id INT PRIMARY KEY,
                                    product VARCHAR,
                                    year DATE,
                                    sale INTEGER);'''

    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    y = 0
    for x in data_json:
        year = data_json[y]['year']
        product = data_json[y]['petroleum_product']
        sale = data_json[y]['sale']
        mySql_insert_query = """INSERT INTO tableyipl (id, product, year, sale)
                                    VALUES (?, ?, ?, ?)"""
        recordTuple = (y , product, year, sale)
        cursor.execute(mySql_insert_query, recordTuple)
        y+=1
    sqliteConnection.commit()
except:
    pass
    
def readSqliteTable():
    try:
        cursor.execute('SELECT DISTINCT product FROM tableyipl')
        # Initializing an empty list to store names of all petroleum products in the database
        all_product=[]
        fetch_products=cursor.fetchall()
        #i is the counter
        i=0
        for pro in fetch_products:
            # Appends the name of petroleum products from database to the list all_product
            all_product.append(pro[i])

        #Selects max year from the table
        sqlite_select_query1 = '''SELECT MAX(year) FROM tableyipl'''
        cursor.execute(sqlite_select_query1)
        #last_year stores the recent/final year from the database table in a list
        last_year=cursor.fetchone()
        sqlite_select_query2 = '''SELECT MIN(year) FROM tableyipl'''
        cursor.execute(sqlite_select_query2)
        #first_year stores the first year from the database table in a list
        first_year=cursor.fetchone()
        print ('{:<30}{:<30}{:<30}{:<30}{:<30}'.format('Product','Year','Min','Max','Avg'))
        #y2 and y1 extracts the first and last year from the lists first_year and last_year respectively
        y2=last_year[0]
        y1=first_year[0]
        #year_diff=5 for report to show data of 5 years interval,
        year_diff=5
        # list_count stores the size for the lists to be made
        list_count=int((y2-y1+1)/year_diff)

        for one_product in all_product:
            # selects a row from database table with one product at a time
            cursor.execute('SELECT * from tableyipl where product=?',(one_product,))
            #totalRows stores all the rows of one_product
            totalRows = cursor.fetchall()
            # min is a list with list_count no. of items with all the items having max system value
            min = [sys.maxsize]*list_count
            max=[0]*list_count
            counter=[0]*list_count
            Average=[0]*list_count
            Total=[0]*list_count
            yr=[0]*list_count
            i=0
            for temp in range(y2,y1-1,-year_diff):
                for row in totalRows:
                    Id = row[0]
                    Product = row[1]
                    Year = row[2]
                    Sale = row[3]
                    # To omit 0 from calculations
                    if(row[3]!=0):
                        if(temp>=Year and Year>temp-year_diff):
                            Total[i]=Total[i]+Sale
                            if(Sale<min[i]):
                                min[i]=Sale
                            if(Sale>max[i]):
                                max[i]=Sale

                            # counter[i] is used to calculate Average by omitting 0's
                            counter[i]+=1
                        # yr[i] stores the year difference
                        yr[i]='{}-{}'.format(temp-year_diff+1,temp)
                if (counter[i]==0):
                    min[i]=0
                else:
                    Average[i]=Total[i]/counter[i]

                print('{:<30}{:<30}{:<30}{:<30}{:<30}'.format(Product,yr[i],min[i],max[i],Average[i]))
                i+=1
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The Sqlite connection is closed")

readSqliteTable()
