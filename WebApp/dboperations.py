## STEP-1 : Importing My SQL Connector
import mysql.connector;

## STEP-2: Establishing connection by "connect" method
connection=mysql.connector.connect(
  user='root',
  password='',
  host='127.0.0.1',
  database='employees'

)

## STEP:3 Creating variable to excecute our query by "Cursor" method
sqlObj= connection.cursor()

## Read data from database of employee by employee number
def get_data(id):
    query = 'SELECT * FROM EMPLOYEES WHERE emp_no='+id
    sqlObj.execute(query)
    rows = sqlObj.fetchall()
    return rows

def insert_data(emp_no,bd,fn,ln,gn,hd):
    ##query = 
    
    ###('+str(emp_no)+','+bd+','+fn+','+str(ln)+','+str(gn)+','+hd+')'
    ###print(query)
    ##sqlObj.execute("INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES ('23','1993-09-12','test','bite','M','1993-09-12')")
    sqlObj.execute("INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES ('"+str(emp_no)+"','"+bd+"','"+fn+"','"+ln+"','"+gn+"','"+hd+"'"+")")
    connection.commit()
    return 1