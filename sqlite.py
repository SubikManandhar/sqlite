import sqlite3
import json
import requests
response = requests.get("https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json")

# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)
data_json=response.json()
# jprint (response.json())
#jprint(a)
y = 0
try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS tablekhali (
                                    id INT PRIMARY KEY,
                                    product VARCHAR,
                                    year DATE,
                                    sale INTEGER);'''

    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()

#    print("SQLite table created")
    for x in data_json:
        year = data_json[y]['year']
        product = data_json[y]['petroleum_product']
        sale = data_json[y]['sale']
        #if (product=="Petrol"):
        mySql_insert_query = """INSERT INTO tablekhali (id, product, year, sale)
                                    VALUES (?, ?, ?, ?) """
        recordTuple = (y , product, year, sale)
        cursor.execute(mySql_insert_query, recordTuple)

        # count = cursor.execute("""INSERT INTO asdfg (id,product, year, sale)  VALUES  (3,'asd','%s','%s')""")
        y+=1
        # break
    sqliteConnection.commit()
    cursor.close()


except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")


    # sqlite_create_table_query = '''CREATE TABLE Diesel (
    #                             id INT PRIMARY KEY,
    #                             product VARCHAR,
    #                             year DATE,
    #                             sale INTEGER);'''
    # cursor.execute(sqlite_create_table_query)
    # sqliteConnection.commit()
    #
    # sqlite_create_table_query = '''CREATE TABLE Kerosene (
    #                             id INT PRIMARY KEY,
    #                             product VARCHAR,
    #                             year DATE,
    #                             sale INTEGER);'''
    # cursor.execute(sqlite_create_table_query)
    # sqliteConnection.commit()
    #
    # sqlite_create_table_query = '''CREATE TABLE Aviation Turbine Fuel (
    #                             id INT PRIMARY KEY,
    #                             product VARCHAR,
    #                             year DATE,
    #                             sale INTEGER);'''
    # cursor.execute(sqlite_create_table_query)
    # sqliteConnection.commit()
    #
    # sqlite_create_table_query = '''CREATE TABLE Light Diesel Oil (
    #                             id INT PRIMARY KEY,
    #                             product VARCHAR,
    #                             year DATE,
    #                             sale INTEGER);'''
    # cursor.execute(sqlite_create_table_query)
    # sqliteConnection.commit()
    #
    # sqlite_create_table_query = '''CREATE TABLE Furnace Oil (
    #                             id INT PRIMARY KEY,
    #                             product VARCHAR,
    #                             year DATE,
    #                             sale INTEGER);'''
    # cursor.execute(sqlite_create_table_query)
    # sqliteConnection.commit()
    #
    # sqlite_create_table_query = '''CREATE TABLE LPG in MT (
    #                             id INT PRIMARY KEY,
    #                             product VARCHAR,
    #                             year DATE,
    #                             sale INTEGER);'''
    # cursor.execute(sqlite_create_table_query)
    # sqliteConnection.commit()
    #
    # sqlite_create_table_query = '''CREATE TABLE Mineral Turpentine Oil (
    #                             id INT PRIMARY KEY,
    #                             product VARCHAR,
    #                             year DATE,
    #                             sale INTEGER);'''
    # cursor.execute(sqlite_create_table_query)
    # sqliteConnection.commit()
