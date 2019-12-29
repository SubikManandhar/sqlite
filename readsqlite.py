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
        cursor.execute('SELECT DISTINCT product FROM tablekhali')
        all_product=[]
        fetch_products=cursor.fetchall()
        i=0
        for pro in fetch_products:
            all_product.append(pro[i])

        sqlite_select_query1 = '''SELECT MAX(year) FROM tablekhali'''
        cursor.execute(sqlite_select_query1)
        last_year=cursor.fetchone()
        sqlite_select_query2 = '''SELECT MIN(year) FROM tablekhali'''
        cursor.execute(sqlite_select_query2)
        first_year=cursor.fetchone()
        print ('{:<30}{:<30}{:<30}{:<30}{:<30}'.format('Product','Year','Min','Max','Avg'))
        y2=last_year[0]
        y1=first_year[0]
        year_diff=5
        list_count=int((y2-y1+1)/year_diff)
        for one_product in all_product:
            cursor.execute('SELECT * from tablekhali where product=?',(one_product,))
            totalRows = cursor.fetchall()
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
                    if(row[3]!=0):
                        if(temp>=Year and Year>temp-year_diff):
                            Total[i]=Total[i]+Sale
                            if(Sale<min[i]):
                                min[i]=Sale
                            if(Sale>max[i]):
                                max[i]=Sale

                            counter[i]+=1
                        yr[i]='{}-{}'.format(temp-year_diff+1,temp)
                if (counter[i]==0):
                    min[i]=0
                else:
                    Average[i]=Total[i]/counter[i]
                            # yr='{}-{}'.format(y-4,y)
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
