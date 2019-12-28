import sqlite3
import sys

def min_value(myList = [], *args):
    min=myList[0]
    for x in myList:
        if(x<min and x!=0):
            min=x
    return min

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db', timeout=20)
        cursor = sqliteConnection.cursor()
        #keep all the products in an list so that we can loop through them easily
        # all_Products=('Petrol','Diesel','Kerosene','Aviation Turbine Fuel','Light Diesel Oil','Furnace Oil','LPG in MT','Mineral Turpentine Oil'  )
        cursor.execute('SELECT DISTINCT product FROM tablekhali')
        all_product=[]
        fetch_products=cursor.fetchall()
        i=0
        for pro in fetch_products:
            all_product.append(pro[i])
        sqlite_select_query1 = '''SELECT MAX(year) FROM tablekhali'''
        cursor.execute(sqlite_select_query1)
        last_year=cursor.fetchone()
        print ('{:<30}{:<30}{:<30}{:<30}{:<30}'.format('Product','Year','Min','Max','Avg'))
        for one_product in all_product:

            cursor.execute('SELECT * from tablekhali where product=?',(one_product,))
            totalRows = cursor.fetchall()
            y=last_year[0]
            # Total=[0]
            # min=[sys.maxsize]
            # max=[0]
            # counter=[0]
            # Average=[0]
            min = [sys.maxsize,sys.maxsize,sys.maxsize]
            max=[0,0,0]
            counter=[0,0,0]
            Average=[0,0,0]
            Total=[0,0,0]
            # i=0

            for row in totalRows:
                if(row[3]!=0):
                    Id = row[0]
                    Product = row[1]
                    Year = row[2]
                    Sale = row[3]
                    if(y>=Year>=y-4):
                        Total[0]=Total[0]+Sale
                        if(Sale<min[0]):
                            min[0]=Sale
                        if(Sale>max[0]):
                            max[0]=Sale
                        counter[0]+=1

                        yr='{}-{}'.format(y-4,y)

                    elif(y-5>=Year>=y-9):
                        Total[1]=Total[1]+Sale
                        if(Sale<min[1]):
                            min[1]=Sale
                        if(Sale>max[1]):
                            max[1]=Sale
                        counter[1]+=1

                        yr1='{}-{}'.format(y-9,y-5)

                    elif(y-10>=Year>=y-14):
                        Total[2]=Total[2]+Sale
                        if(Sale<min[2]):
                            min[2]=Sale
                        if(Sale>max[2]):
                            max[2]=Sale
                        counter[2]+=1

                        yr2='{}-{}'.format(y-14,y-10)

            if(counter[0] == 0):
                # Average[0]=0
                min[0]=0
            else:
                Average[0]=Total[0]/counter[0]
            if(counter[1] == 0):
                # Average[1]=0
                min[1]=0
            else:
                Average[1]=Total[1]/counter[1]
            if(counter[2] == 0):
                # Average[2]=0
                min[2]=0
            else:
                Average[2]=Total[2]/counter[2]

            print ('{:<30}{:<30}{:<30}{:<30}{:<30}'.format(Product,yr,min[0],max[0],Average[0]))
            print ('{:<30}{:<30}{:<30}{:<30}{:<30}'.format(Product,yr1,min[1],max[1],Average[1]))
            print ('{:<30}{:<30}{:<30}{:<30}{:<30}'.format(Product,yr2,min[2],max[2],Average[2]))


            # i+=1
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The Sqlite connection is closed")

readSqliteTable()
