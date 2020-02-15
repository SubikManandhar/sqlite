# Petroleum-report
The database name and the table name must be unique.
Variables used described uisng comments in the program itself

## Requirements
python 3.7 is preferred


### Unit Tests
*First checking if there exists a table named 'tableyipl' or any table_name assigned to the table, and inserting into the table table_name if table is empty by using try except block.
*Using try except to calculte min,max and average of each petroleum product for 5 years interval.
*Using for loops to fetch datas from newly stored sqlite database
*Using if statement for omitting 0's from the calculations.
*Using counter[] list to make sure that average is calculated without 0's

#### Running the app

```bash
python report.py
```
If the program doesn't run then try 
```bash
python3 report.py
```
OR
```bash
python3.7 report.py
```
