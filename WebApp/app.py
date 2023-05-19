## importing flask
from flask import Flask,render_template,request
## Declare a Flask app
app = Flask(__name__)
## import dboperations functions
from dboperations import get_data,insert_data
# importing the random module
import random






## route function in Flask

## Syntax: basedomain/ ,basedomain/home ,Localhost:5000/home
## @app.route("/"),@app.route("/home")

@app.route("/home")
def main():
    return render_template('index.html')

## Add Page route
@app.route("/add")
def add():
    return render_template('add.html')

## update page route
@app.route("/update")
def update():
    return render_template('update.html')

## delete page route
@app.route("/delete")
def delete():
    return render_template('delete.html')

@app.route("/find",methods=["POST","GET"])
def find():
    emp_id = request.form["Id"]
    print(emp_id)
    data = get_data(emp_id)
    print(data)
    return render_template('index.html',
                           fn=data[0][2],ln=data[0][3],
                           en=data[0][0],gn=data[0][4],
                           hd=data[0][5]
                           
                           )

@app.route("/insert",methods=["POST","GET"])
def insert():
    emp_no=random.randint(0,10000)
    bd=request.form["bd"]
    fn=request.form["fn"]
    ln=request.form["ln"]
    gn=request.form["gn"]
    hd=request.form["bd"]
    print(emp_no,bd,fn,ln,gn,hd)
    insert_data(emp_no,bd,fn,ln,gn,hd)
    return render_template('add.html')




## Call the Flask app

if __name__ =="__main__":
  app.run()


